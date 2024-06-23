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

    class Meta:
        ordering = ['surname']


class Student(Profile):
    group = models.CharField(max_length=5)
    studying_mode = models.CharField(max_length=5)
    studying_year = models.IntegerField
    major = models.CharField(max_length=50)
    choices = models.ManyToManyField('Choice', related_name='student_choices', null=True, blank=True)

    class Meta:
        # ordering = ['group']
        permissions = [
            ('view_my_performance', 'Can view My Performance section'),
        ]

    def __str__(self):
        return f'{self.surname} {self.name}'


class Lecturer(Profile):
    title = models.CharField(max_length=50)

    class Meta:
        permissions = [
            ('view_grades', 'Can view Grades section'),
            ('add_grades', 'Can add grades to Grades section'),
            ('edit_grades', 'Can edit grades in Grades section'),
            ('delete_grades', 'Can delete grades in Grades section')
        ]

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
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    body = models.TextField()
    sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:300]


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, null=True)
    grade = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.grade}'


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(null=True)
    # student = models.ManyToManyField(Student)

    def __str__(self):
        return self.choice_text
