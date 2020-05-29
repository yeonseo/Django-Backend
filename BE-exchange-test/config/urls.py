"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# REST 이용
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('freeboards/', include('freeboards.urls')),
    path('users/', include('users.urls')),
    path('movies/', include('movies.urls')),
    path('reservations/', include('reservations.urls')),
    path('rooms/', include('rooms.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^(?P<path>.*)$', TemplateView.as_view(template_name='index.html')),
]

# 만약 개발중이라면, 내 폴더 안의 파일들을 제공하게 작성
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # 니꼬's urls
# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
#
#
# def trigger_error(request):
#     division_by_zero = 1 / 0
#
#
# urlpatterns = [
#     path("", include("core.urls", namespace="core")),
#     path("rooms/", include("rooms.urls", namespace="rooms")),
#     path("users/", include("users.urls", namespace="users")),
#     path("reservations/", include("reservations.urls", namespace="reservations")),
#     path("reviews/", include("reviews.urls", namespace="reviews")),
#     path("lists/", include("lists.urls", namespace="lists")),
#     # path("conversations/", include("conversations.urls", namespace="conversations")),
#     path("admin/", admin.site.urls),
#     # path("sentry-debug/", trigger_error),
#
#     path('freeboards/', include('freeboards.urls')),
# ]
#
#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)