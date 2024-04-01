from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import LikeSerializer

class LikeCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = LikeSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikeDeleteView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def delete(self, request):
        if 'product' not in request.data:
            return Response({'message': 'Field "post" is required'})
        product = request.data.get('product')
        user = request.user
        like = user.likes.filter(post=product)
        if not like.exists():
            return Response({'message': 'You haven\'t liked this post'}, status=400)
        like.delete()
        return Response({'message': 'deleted'}, status=204)