from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie  # 모델 설정
        fields = ('id', 'title', 'genre', 'year')

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie  # 모델 설정
        fields = ('id', 'title', 'genre', 'year')

class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie  # 모델 설정
        fields = ('id', 'title', 'genre', 'year')
