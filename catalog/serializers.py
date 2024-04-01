from rest_framework import serializers
from catalog.models import Catalog

class CatalogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ('id', 'name')


class CatalogSerializer(serializers.ModelSerializer):
    children = CatalogListSerializer(many=True, read_only=True)
