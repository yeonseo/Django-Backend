from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from . import views
from rest_framework.routers import DefaultRouter

app_name = "users"

router = DefaultRouter()
router.register('', views.LoginViewSet)


urlpatterns = [
    url('api-auth/', include('rest_framework.urls')),
    url(r'^$', views.LoginViewSet.as_view(), name='users'),
    url("login/", views.LoginView.as_view(), name="login"),
    url("login/github/", views.github_login, name="github-login"),
    url("login/github/callback/", views.github_callback, name="github-callback"),
    url("login/kakao/", views.kakao_login, name="kakao-login"),
    url("login/kakao/callback/", views.kakao_callback, name="kakao-callback"),
    url("logout/", views.log_out, name="logout"),
    url("sigup/", views.SignUpView.as_view(), name="signup"),
    url(
        "verify/<str:key>/", views.complete_verification, name="complete-verification"
    ),
    url("update-profile/", views.UpdateProfileView.as_view(), name="update"),
    url("update-password/", views.UpdatePasswordView.as_view(), name="password"),
    url("<int:pk>/", views.UserProfileView.as_view(), name="profile"),
    url("switch-hosting/", views.switch_hosting, name="switch-hosting"),
    url("switch-language/", views.switch_language, name="switch-language"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
