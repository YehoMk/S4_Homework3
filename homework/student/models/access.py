from django.db import models

from .student import Student


__all__ = ("Access",)


class Access(models.Model):
    start_date = models.DateTimeField(auto_now=True, null=False)
    end_date = models.DateTimeField(null=False)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="access")
