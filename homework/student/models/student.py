from django.db import models

from .group import Group


__all__ = ("Student",)


class Student(models.Model):
    name = models.CharField(null=False, max_length=80)
    surname = models.CharField(null=False, max_length=80)
    student_id = models.IntegerField(unique=True, null=False)
    email = models.EmailField(unique=True, null=False)
    age = models.IntegerField(null=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="students")
