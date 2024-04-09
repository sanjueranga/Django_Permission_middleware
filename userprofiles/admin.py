from django.contrib import admin
from .models import Role,Permission


class RoleAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

class PermissionAdmin(admin.ModelAdmin):
    list_display=("id","permission")


admin.site.register(Role, RoleAdmin)
admin.site.register(Permission,PermissionAdmin)
