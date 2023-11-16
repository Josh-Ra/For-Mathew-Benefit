from django.db import models
from django.db.models.query import QuerySet

# Create your models here.


class Active_Manager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super(Active_Manager, self).get_queryset().filter(is_active=True)


class People(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"
