from rest_framework import serializers

from post.models import Post, PostImage


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    comments_count = serializers.ReadOnlyField(source='comments.count')

    class Meta:
        model = Post
        fields = ('id', 'title', 'owner', 'owner_username',
                  'category', 'category_name', 'preview', 'comments_count', 'likes_count')

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        user = self.context.get('request').user
        repr['is_liked'] = user.likes.filter(post=instance).exists()
        return repr


class PostCreateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    images = PostImageSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        # print(request.FILES, '!!!!!!!!!!')
        images = request.FILES.getlist('images')
        post = Post.objects.create(**validated_data)
        image_objects = [
            PostImage(image=image, post=post) for image in images]
        PostImage.objects.bulk_create(image_objects)
        return post


class PostDetailSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    comments_count = serializers.ReadOnlyField(source='comments.count')
    images = PostImageSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = '__all__'

