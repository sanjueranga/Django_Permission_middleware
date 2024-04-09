from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationAPIView, UserLoginApiView

router = DefaultRouter()

urlpatterns = [
    path("register/", UserRegistrationAPIView.as_view(), name="user-registration"),
    path("login/", UserLoginApiView.as_view(), name="user-login"),
]


urlpatterns = router.urls + urlpatterns
