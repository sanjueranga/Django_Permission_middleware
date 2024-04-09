from rest_framework import status, generics, permissions
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer
from .permissions import CanEditCoursePermission


class EditCourseAPIView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [CanEditCoursePermission]

    def put(self, request, *args, **kwargs):
        course_id = kwargs.get("pk")
        try:
            course = self.get_queryset().get(pk=course_id)
        except Course.DoesNotExist:
            return Response(
                {"message": "Course not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(course, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)
