from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Student, Lecturer, Post, Comment, Message, Grade

admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(Grade)
