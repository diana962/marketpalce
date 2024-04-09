from rest_framework import serializers

from product.models import Clothes
from .models import Order
from product.serializers import ClothesListSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ClothesListSerializer()
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Order
        fields = ['id', 'product', 'owner', 'quantity', 'created_at', 'status']
        read_only_fields = ['created_at']

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        product = Clothes.objects.get_or_create(**product_data)[0]
        order = Order.objects.create(product=product, **validated_data)
        return order
