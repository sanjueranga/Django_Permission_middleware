from django.urls import path
from .views import EditCourseAPIView

urlpatterns = [
    path("edit-course/<int:pk>/", EditCourseAPIView.as_view(), name="edit_course"),
]
