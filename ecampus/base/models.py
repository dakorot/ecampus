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


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:300]
