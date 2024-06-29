from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Student
from .serializers import StudentSerializer, StudentChoiceSerializer


@api_view(['GET'])
def get_routes(request):
    routes = [
        'GET /api',
        'GET /api/students',
        'GET /api/students/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def get_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_student(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_choices(request):
    students = Student.objects.all()
    serializer = StudentChoiceSerializer(students, many=True)
    return Response(serializer.data)
