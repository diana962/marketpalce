from rest_framework import serializers
from like.models import Like, Favorite


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = '__all__'

    def validate(self, attrs):
        user = self.context['request'].user
        product = attrs['product']
        if user.likes.filter(post=product).exists():
            raise serializers.ValidationError('You already liked it once!')
        return attrs


class FavoriteSerializer(serializers.ModelSerializer):
    product_title = serializers.ReadOnlyField(source='product.title')
    class Meta:
        model = Favorite
        fields = ('id', 'product', 'product_title')

