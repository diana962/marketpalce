from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    product = serializers.ReadOnlyField(source='product.id')

    class Meta:
        model = Rating
        fields = '__all__'

