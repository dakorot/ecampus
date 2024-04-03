from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)
    group = models.CharField(max_length=5)
    studying_mode = models.CharField(max_length=5)
    studying_year = models.IntegerField
    major = models.CharField(max_length=50)
    # description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.name, self.surname
