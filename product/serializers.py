from rest_framework import serializers
from product.models import Clothes
from catalog.models import Catalog
# from comment.serializers import CommentSerializer
from product.models import ClothesImage


class ClothesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothesImage
        fields = '__all__'


class ClothesListSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='catalog.name')
    likes_count = serializers.ReadOnlyField(source='likes.count')

    class Meta:
        model = Clothes
        fields = '__all__'
        # fields = ('id', 'title', 'owner', 'owner_username', 'category',
        #           'category_name', 'preview', 'images', 'likes_count', 'comments_count')

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        user = self.context.get('request').user
        if user.is_authenticated:
            repr['is_liked'] = user.likes.filter(post=instance).exists()
        return repr


class ClothesCreateSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(required=True, queryset=Catalog.objects.all())
    owner = serializers.ReadOnlyField(source='owner.id')
    images = ClothesImageSerializer(many=True, required=False)

    class Meta:
        model = Clothes
        fields = ('id', 'title', 'owner', 'category', 'preview', 'images')

    def create(self, validated_data):
        request = self.context.get('request')
        # print(request.FILES, '!!!')
        images = request.FILES.getlist('images')
        product = Clothes.objects.create(**validated_data)
        image_objects = [ClothesImage(image=image, post=product) for image in images]
        ClothesImage.objects.bulk_create(image_objects)
        return product


class ClothesDetailSerializers(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name')
    likes_count = serializers.ReadOnlyField(source='likes.count')
    images = ClothesImageSerializer(many=True, required=False)

    class Meta:
        model = Clothes
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        user = self.context.get('request').user
        repr['is_liked'] = user.likes.filter(post=instance).exists()
        return repr
