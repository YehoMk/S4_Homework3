from django.db import models


__all__ = ("Literature",)


class Literature(models.Model):
    name = models.CharField(null=False, max_length=80)
    genre = models.CharField(null=False, max_length=50)
    release_date = models.DateTimeField(null=False)
    Author = models.CharField(null=False, max_length=240)
