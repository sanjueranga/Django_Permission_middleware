from rest_framework import permissions
from courses.models import Course, CourseUserMap, CoursePermission


class CanEditCoursePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        course_pk = view.kwargs.get("pk")
        try:
            course = Course.objects.get(pk=course_pk)
        except Course.DoesNotExist:
            return False
        try:
            course_user_map = CourseUserMap.objects.get(
                course=course, user=request.user
            )
            user_role = course_user_map.role.name
        except CourseUserMap.DoesNotExist:
            return False

        if CoursePermission.objects.filter(
            course=course,
            role__name=user_role,
            permission__permission="Edit Course",
        ).exists():
            return True
        return False
