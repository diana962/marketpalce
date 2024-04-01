from rest_framework import generics, permissions

from product.permission import CommentsDeletePermission
from .models import Comment
from . import serializer


class CommentCreateView(generics.CreateAPIView):
    serializer_class = serializer.CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetailView(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializer.CommentSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [CommentsDeletePermission(), ]
        return [permissions.IsAdminUser()]
