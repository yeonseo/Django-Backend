from django.conf.urls   import url
from .views import *


urlpatterns = [
    url(r'^test3/$', Test3.as_view(), name=Test3.name),
    url(r'^test4/$', Test4.as_view(), name=Test4.name),
]