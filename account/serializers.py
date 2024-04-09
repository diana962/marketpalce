from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()
class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        write_only=True,
        max_length=40,
        min_length=8
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        print(attrs, type(attrs))
        password2 = attrs.pop('password2')
        if attrs['password'] != password2:
            raise serializers.ValidationError('Пароли не совпадают!')
        validate_password(attrs['password'])
        return attrs



class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("__all__")