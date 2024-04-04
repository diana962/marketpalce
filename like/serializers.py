from rest_framework import serializers
from like.models import Like

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


# class FavoriteSerializer(serializers.ModelSerializer):
#     post_title = serializers.ReadOnlyField(source='post.title')
#     # post_preview = serializers.ReadOnlyField(source='post.preview.url')
#     class Meta:
#         model = Favorite
#         fields = ('id', 'post', 'post_title')
#
#     def to_representation(self, instance):
#         repr = super(FavoriteSerializer, self).to_representation(instance)
#         preview = instance.post.preview
#         repr['post_preview'] = preview.url if preview else None
#         return repr

