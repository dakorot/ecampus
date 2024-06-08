from django.forms import ModelForm
from .models import Post, Comment, Message, Grade


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['author']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        exclude = ['sender']


class GradeForm(ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'grade']
