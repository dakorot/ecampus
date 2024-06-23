from django.forms import ModelForm, Form, ModelMultipleChoiceField, HiddenInput, CheckboxSelectMultiple, \
    ModelChoiceField
from .models import Post, Comment, Message, Grade, Question, Choice


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


class VoteForm(Form):
    choices = ModelMultipleChoiceField(
        queryset=None,
        widget=CheckboxSelectMultiple()
    )

    def __init__(self, *args, **kwargs):
        question_id = kwargs.pop('question_id', None)
        super().__init__(*args, **kwargs)

        if question_id:
            self.fields['choices'].queryset = Choice.objects.filter(question_id=question_id)
