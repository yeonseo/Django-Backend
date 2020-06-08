from rest_framework import serializers
from .models import FreeBoard
from users import models as user

class UserField(serializers.RelatedField):
    def get_username(self):
        return 'username : ' % (user.username)

class FreeBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeBoard  # 모델 설정
        fields = ('id', 'username', 'title', 'created', 'board_type', 'views')

class FreeBoardDetailSerializer(serializers.ModelSerializer):
    username = serializers.HyperlinkedIdentityField(view_name='board_detail', lookup_field='username', many=True, read_only=True)
    class Meta:
        model = FreeBoard  # 모델 설정
        fields = ('id', 'username', 'title', 'created', 'updated', 'board_type', 'views', 'content', 'files')

class FreeBoardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeBoard  # 모델 설정
        fields = ('id', 'username', 'title', 'board_type', 'content', 'views', 'files')
