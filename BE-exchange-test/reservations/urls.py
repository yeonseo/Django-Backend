from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'reservations'

urlpatterns = [
    url('api-auth/', include('rest_framework.urls')),
    url(r'^(?P<id>\d+)/$', views.ReservationDetailView.as_view(), name='reservations_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # 니꼬's
# from django.urls import path
# from . import views
#
# app_name = "reservations"
#
# urlpatterns = [
#     path(
#         "create/<int:room>/<int:year>-<int:month>-<int:day>",
#         views.create,
#         name="create",
#     ),
#     path("<int:pk>/", views.ReservationDetailView.as_view(), name="detail"),
#     path("<int:pk>/<str:verb>", views.edit_reservation, name="edit"),
# ]