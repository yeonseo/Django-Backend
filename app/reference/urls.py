from django.conf.urls   import url
from .views import *


urlpatterns = [
    url(r'^test1/$', Test1.as_view(), name=Test1.name),
    url(r'^test2/$', Test2.as_view(), name=Test2.name),
]