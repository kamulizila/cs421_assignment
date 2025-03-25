from django.urls import path
from .views import student_list, subject_list
from . import views

urlpatterns = [
    path('students/', student_list, name='student-list'),
    path('subjects/', subject_list, name='subject-list'),
     path('', views.home, name='home'),  # Root URL pattern
    
]