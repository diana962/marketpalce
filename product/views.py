from rest_framework import generics, permissions, response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from product.models import Clothes
from product import serializers
from product.permission import IsOwner, IsOwnerOrAdmin
from rating.serializer import RatingSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ClothesViewSet(ModelViewSet):
    queryset = Clothes.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('title', 'body')
    filter_set_fields = ('owner', 'category')
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ClothesListSerializer
        elif self.action in ('create', 'update', 'partial_update'):
            return serializers.ClothesCreateSerializer
        return serializers.ClothesDetailSerializers

    def get_permissions(self):
        # only admin or the owner can delete a post
        if self.action == 'destroy':
            return [IsOwnerOrAdmin(), ]
        # only owner can update a post
        elif self.action in ('update', 'partial_update'):
            return [IsOwner(), ]
        # other users can watch and create posts
        return [permissions.IsAuthenticatedOrReadOnly(), ]

    # /api/v1/products/<id>/rating/
    @action(['GET', 'POST', 'DELETE'], detail=True)
    def rating(self, request, pk):
        product = self.get_object()
        user = request.user
        is_rating = product.ratings.filter(owner=user).exists()

        if request.method == 'GET':
            rating = product.ratings.all()
            serializers = RatingSerializer(instance=rating, many=True)
            return response.Response(serializers.data, status=200)

        elif request.method == 'POST':
            if is_rating:
                return response.Response('You already rated this product',
                                         status=400)
            data = request.data
            serializer = RatingSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save(owner=user, product=product)
            return response.Response(serializer.data, status=201)

        else:
            if not is_rating:
                return response.Response('You didn\'t rated this product',
                                         status=400)
            rating = product.ratings.get(owner=user)
            rating.delete()
            return response.Response('Deleted!', status=204)


