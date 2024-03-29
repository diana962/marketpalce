from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True, max_length=150)
    last_name = serializers.CharField(required=True, max_length=150)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        min_length=8, write_only=True, required=True)
    password2 = serializers.CharField(
        min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('groups', 'user_permissions', 'is_superuser', 'is_staff', 'is_active')

    def validate(self, attrs):
        password2 = attrs.pop('password2')
        if password2 != attrs['password']:
            raise serializers.ValidationError('Passwords didn\'t match!')
        validate_password(attrs['password'])
        return attrs

    def validate_first_name(self, value):
        if not value.istitle():
            raise serializers.ValidationError('Name must start with uppercase letter!')
        return value

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',  "is_staff", "user_permissions")