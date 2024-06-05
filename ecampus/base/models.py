from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLES = (
        ('ADMIN', 'Admin'),
        ('STUDENT', 'Student'),
        ('LECTURER', 'Lecturer')
    )

    role = models.CharField(max_length=10, choices=ROLES)


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=10, choices=User.ROLES)


class Student(Profile):
    group = models.CharField(max_length=5)
    studying_mode = models.CharField(max_length=5)
    studying_year = models.IntegerField
    major = models.CharField(max_length=50)
    # description = models.TextField(null=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Lecturer(Profile):
    title = models.CharField(max_length=50)
    # description = models.TextField(null=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


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


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    body = models.TextField()
    sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:300]


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    grade = models.IntegerField(null=True)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.grade}'
