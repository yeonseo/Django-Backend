from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from . import views
from rest_framework.routers import DefaultRouter


app_name = 'freeboards'

router = DefaultRouter()
router.register('', views.FreeboardsViewSet)

urlpatterns = [
    url('api-auth/', include('rest_framework.urls')),
    url(r'^$', views.FreeboardsFilterOfType.as_view(), name='boards list'),
    url(r'^create/$', views.FreeboardsCreate.as_view(), name='boards create'),
    url(r'^(?P<id>\d+)/$', views.FreeboardsDetail.as_view(), name='boards detail'),
    url(r'^(?P<id>\d+)/update/$', views.FreeboardsUpdate.as_view(), name='boards update'),
    url(r'^(?P<id>\d+)/delete/$', views.FreeboardsDelete.as_view(), name='boards delete'),
    url(r'^(?P<board>\d+)/comment_create/$', views.CommentCreate.as_view(), name='comment create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

