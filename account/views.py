from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from account.send_mail import send_mail_register
from account.serializers import UserRegisterSerializer, UserListSerializer, \
    UserActivationSerializer


User = get_user_model()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSerializer
        if self.action == 'activate':
            return UserActivationSerializer
        return UserListSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        code = user.activation_code
        email = user.email
        send_mail_register(email, code)

    # http: // 127.0.0.1: 8000 / accounts / activate /
    @action(methods=['POST'], detail=False)
    def activate(self, request):
        activation_code = request.data.get('activation_code')

        if not activation_code:
            return Response({'error': 'Activation code not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(activation_code=activation_code)
        except User.DoesNotExist:
            return Response({'error': 'Invalid activation code'}, status=status.HTTP_404_NOT_FOUND)

        user.is_active = True
        user.save()

        return Response({'message': 'User activated successfully'})

    @action(['GET'], detail=False, url_path='activate/(?P<uuid>[0-9A-Fa-f-]+)')
    def activate(self, request, uuid):
        try:
            user = User.objects.get(activation_code=uuid)
        except User.DoesNotExist:
            return Response({'msg': 'Invalid Link or Link expired'}, status=400)

        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response({'msg': 'Account activated!'}, status=200)
