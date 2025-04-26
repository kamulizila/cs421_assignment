from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

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
    return Response({"count": students.count(), "data": serializer.data})

@api_view(['GET'])
def subject_list(request):
    # Get subjects for Software Engineering program
    subjects = Subject.objects.filter(program="Software Engineering").order_by('year')
    
    # Group by year and count unique subjects
    result = {}
    subject_count = 0  # Track total unique subjects
    
    for subject in subjects:
        year_key = f"Year {subject.year}"
        
        if year_key not in result:
            result[year_key] = []

        if subject.name not in result[year_key]:  # Prevent duplicates within the same year
            result[year_key].append(subject.name)
            subject_count += 1  # Count only unique subjects

    return JsonResponse({"count": subject_count, "data": result})

from django.http import JsonResponse

def health_check(request):
    return JsonResponse({"status": "ok"}, status=200)