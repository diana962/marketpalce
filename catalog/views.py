from catalog.models import Catalog
from catalog import serializers
from rest_framework import generics, permissions


class CatalogCreateListView(generics.ListCreateAPIView):
    queryset = Catalog.objects.all()
    serializer_class = serializers.CatalogListSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated(), ]
        return [permissions.IsAdminUser(), ]
