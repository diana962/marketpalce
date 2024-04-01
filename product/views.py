from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from product.models import Clothes
from product import serializers
from product.permissions import IsOwner, IsOwnerOrAdmin


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
        # only admin or the owner csn delete a post
        if self.action == 'destroy':
            return [IsOwnerOrAdmin(), ]
        # only owner can update a post
        elif self.action in ('update', 'partial_update'):
            return [IsOwner(), ]
        # other users can watch and create posts
        return [permissions.IsAuthenticatedOrReadOnly(), ]
