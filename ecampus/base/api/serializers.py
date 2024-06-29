from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from base.models import Choice, Student


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    surname = serializers.CharField(max_length=50)
    faculty = serializers.CharField(max_length=50)
    created = serializers.DateTimeField()
    role = serializers.CharField(max_length=10)
    group = serializers.CharField(max_length=5)
    studying_mode = serializers.CharField(max_length=5)
    studying_year = serializers.IntegerField
    major = serializers.CharField(max_length=50)


class ChoiceSerializer(ModelSerializer):
    choice_text = serializers.CharField(max_length=200)

    class Meta:
        model = Choice
        fields = ['choice_text']


class StudentChoiceSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'surname', 'faculty', 'group', 'choices']
