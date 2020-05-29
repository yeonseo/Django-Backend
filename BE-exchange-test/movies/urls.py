from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'movies'

urlpatterns = [
    url('api-auth/', include('rest_framework.urls')),
    url(r'^$', views.MovieViewSet.as_view(), name='movies_list'),
    url(r'^create/$', views.MovieCreate.as_view(), name='movies_create'),
    url(r'^(?P<id>\d+)/$', views.MovieDetail.as_view(), name='movies_detail'),
    url(r'^(?P<id>\d+)/update/$', views.MovieUpdate.as_view(), name='movies_update'),
    url(r'^(?P<id>\d+)/delete/$', views.MovieDelete.as_view(), name='movies_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)