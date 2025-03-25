from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the CS421 Assignment!")

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Subject
from .serializers import StudentSerializer, SubjectSerializer
from django.http import JsonResponse

@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()[:10]  # Get first 10 students
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def subject_list(request):
    # Get subjects for Software Engineering program
    subjects = Subject.objects.filter(program="Software Engineering").order_by('year')
    
    # Group by year
    result = {}
    for subject in subjects:
        year_key = f"Year {subject.year}"
        if year_key not in result:
            result[year_key] = []
        result[year_key].append(subject.name)
    
    return JsonResponse(result)