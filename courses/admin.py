from django.contrib import admin
from .models import Course, CourseUserMap, CoursePermission


class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "code", "description")


class CoursePermissionAdmin(admin.ModelAdmin):
    list_display = ("course", "role", "permission")


class CourseUserMapAdmin(admin.ModelAdmin):
    list_display = ("course", "user", "role")


admin.site.register(Course, CourseAdmin)
admin.site.register(CoursePermission, CoursePermissionAdmin)
admin.site.register(CourseUserMap, CourseUserMapAdmin)
