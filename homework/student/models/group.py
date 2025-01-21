from django.db import models


__all__ = ("Group",)


class Group(models.Model):
    name = models.CharField(null=False, max_length=100)
    moto = models.CharField(null=False, max_length=100)
    classroom = models.IntegerField(null=False)
