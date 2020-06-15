from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import FreeBoard
from .serializers import FreeBoardSerializer, FreeBoardDetailSerializer, FreeBoardCreateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import status


class FreeboardsViewSet(ListAPIView):
    serializer_class = FreeBoardSerializer
    queryset = FreeBoard.objects.all()

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]

    filter_fields = ['board_type']
    search_fields = ['title', 'content']

class FreeboardsDetail(RetrieveAPIView):
    lookup_field = 'id'
    queryset = FreeBoard.objects.all()
    serializer_class = FreeBoardDetailSerializer

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]

    filter_fields = ['board_type']
    search_fields = ['title', 'content']

class FreeboardsUpdate(UpdateAPIView):
    lookup_field = 'id'
    queryset = FreeBoard.objects.all()
    serializer_class = FreeBoardCreateSerializer

    def update(self, request, *args, **kwargs):
        # user id 반영 추가
        request.data['username'] = request.user.id

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class FreeboardsDelete(DestroyAPIView):
    lookup_field = 'id'
    queryset = FreeBoard.objects.all()
    serializer_class = FreeBoardSerializer

class FreeboardsCreate(CreateAPIView):
    queryset = FreeBoard.objects.all()
    serializer_class = FreeBoardCreateSerializer

    def create(self, request, *args, **kwargs):
        # user id 반영 추가
        request.data['username'] = request.user.id

        # 기존코드
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class FreeboardsFilterOfValue(ListAPIView):
    filter = 2
    queryset = FreeBoard.objects.filter(board_type=filter)
    serializer_class = FreeBoardDetailSerializer

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]

    filter_fields = ['board_type']
    search_fields = ['title', 'content']

class FreeboardsFilterOfType(ListAPIView):

    def get_queryset(self, board_type=None):
        queryset = FreeBoard.objects.order_by('-id')
        if board_type:
            queryset = queryset.filter(board_type=board_type)
        return queryset

    def get_serializer(self, *args, **kwargs):
        serializer_class = FreeBoardDetailSerializer
        return serializer_class(*args, **kwargs)

    def list(self, request, *args, **kwargs):
        board_type = request.query_params.get("board_type", None)
        queryset = self.filter_queryset(self.get_queryset(board_type))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @permission_classes((IsAuthenticated,))
    @authentication_classes((JSONWebTokenAuthentication,))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
