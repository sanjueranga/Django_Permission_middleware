from django.contrib.auth.models import User
from django.db import models
from userprofiles.models import Role
from userprofiles.models import Permission


# Model for Course
class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.title


class CoursePermission(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("course", "role", "permission")

    def __str__(self):
        return f"{self.course.title} - {self.role.name} - {self.permission.permission}"


# Model for CourseUserMap
class CourseUserMap(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("course", "user")

    def __str__(self):
        return f"{self.user.username} - {self.course.title} - {self.role.name}"
