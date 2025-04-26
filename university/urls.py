from django.urls import path
from .views import student_list, subject_list
from . import views
from .views import health_check


urlpatterns = [
    path('api/students/', student_list, name='student-list'),
    path('api/subjects/', subject_list, name='subject-list'),
    path('', views.home, name='home'),  # Root URL pattern
     path('health/', health_check, name='health_check'),
    
]
