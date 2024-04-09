from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from account.send_mail import send_mail_register
from account.serializers import UserRegisterSerializer, UserListSerializer

User = get_user_model()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSerializer
        return UserListSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        code = user.activation_code
        email = user.email
        send_mail_register(email, code)





