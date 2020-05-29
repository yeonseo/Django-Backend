from .serializers import MovieSerializer, MovieDetailSerializer, MovieCreateSerializer
from .models import Movie
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView


class MovieViewSet(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer

class MovieUpdate(UpdateAPIView):
    lookup_field = 'id'
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDelete(DestroyAPIView):
    lookup_field = 'id'
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieCreate(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieCreateSerializer