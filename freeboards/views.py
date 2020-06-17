from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        # view +1 반영 추가
        request.data['username'] = instance.username
        request.data['title'] = instance.title
        request.data['content'] = instance.content
        instance.views = instance.views + 1
        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

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

    def delete(self, request, *args, **kwargs):
        request_user = request.user.id
        instance = self.get_object()
        board_user = instance.username
        if request_user == board_user:
            return self.destroy(request, *args, **kwargs)
        else:
            content = {'수정 권한 오류': '작성자 정보와 일치하지 않습니다.'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

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
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filter_fields = ['board_type', 'username']
    search_fields = ['title', 'content', 'username__username']

    def get_queryset(self, board_type=None):
        queryset = FreeBoard.objects.order_by('-id')
        if board_type:
            queryset = queryset.filter(board_type=board_type)
        return queryset

    # def filter_queryset(self, request, queryset, view):
    #     search_fields = self.get_search_fields(view, request)
    #     search_terms = self.get_search_terms(request)
    #
    #     if not search_fields or not search_terms:
    #         return queryset
    #
    #     orm_lookups = [
    #         self.construct_search(str(search_field))
    #         for search_field in search_fields
    #     ]
    #
    #     base = queryset
    #     conditions = []
    #     for search_term in search_terms:
    #         queries = [
    #             models.Q(**{orm_lookup: search_term})
    #             for orm_lookup in orm_lookups
    #         ]
    #         conditions.append(reduce(operator.or_, queries))
    #     queryset = queryset.filter(reduce(operator.and_, conditions))
    #
    #     if self.must_call_distinct(queryset, search_fields):
    #         # Filtering against a many-to-many field requires us to
    #         # call queryset.distinct() in order to avoid duplicate items
    #         # in the resulting queryset.
    #         # We try to avoid this if possible, for performance reasons.
    #         queryset = distinct(queryset, base)
    #     return queryset

    # def filter_queryset(self, queryset):
    #     """
    #     Given a queryset, filter it with whichever filter backend is in use.
    #
    #     You are unlikely to want to override this method, although you may need
    #     to call it either from a list view, or from a custom `get_object`
    #     method if you want to apply the configured filtering backend to the
    #     default queryset.
    #     """
    #
    #     filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    #     for backend in list(filter_backends):
    #         queryset = backend().filter_queryset(self.request, queryset, self)
    #     return queryset

    def get_serializer_class(self):
        serializer_class = FreeBoardDetailSerializer
        return serializer_class

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