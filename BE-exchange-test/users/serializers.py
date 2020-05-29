from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # 모델 설정
        fields = ('id', 'username', 'email', 'password')

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'date_joined', 'avatar', 'gender', 'bio', 'birthdate',
                  'language', 'is_superuser', 'is_staff')

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')