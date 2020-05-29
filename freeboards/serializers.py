from rest_framework import serializers
from .models import FreeBoard

class FreeBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeBoard  # 모델 설정
        fields = ('id', 'username', 'title', 'created', 'board_type', 'views')

class FreeBoardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeBoard  # 모델 설정
        fields = ('id', 'username', 'title', 'created', 'updated', 'board_type', 'views', 'content', 'files')

class FreeBoardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeBoard  # 모델 설정
        fields = ('id', 'username', 'title', 'board_type', 'content', 'views' , 'files')
