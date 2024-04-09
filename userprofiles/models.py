from django.db import models


# Model for Role
class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Permission(models.Model):
    permission = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.permission
