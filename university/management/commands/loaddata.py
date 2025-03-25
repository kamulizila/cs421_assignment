from django.core.management.base import BaseCommand
from university.models import Student, Subject

class Command(BaseCommand):
    help = 'Load initial data into database'

    def handle(self, *args, **options):
        # Students data
        students = [
            {'name': 'John Doe', 'program': 'Software Engineering'},
            {'name': 'Jane Smith', 'program': 'Computer Science'},
            {'name': 'Michael Johnson', 'program': 'Software Engineering'},
            {'name': 'Emily Davis', 'program': 'Information Technology'},
            {'name': 'Robert Brown', 'program': 'Software Engineering'},
            {'name': 'Sarah Wilson', 'program': 'Computer Science'},
            {'name': 'David Taylor', 'program': 'Software Engineering'},
            {'name': 'Jessica Anderson', 'program': 'Information Technology'},
            {'name': 'Thomas Martinez', 'program': 'Software Engineering'},
            {'name': 'Lisa Robinson', 'program': 'Computer Science'},
        ]

        # Subjects data
        subjects = [
            {'program': 'Software Engineering', 'year': 1, 'name': 'Introduction to Programming'},
            {'program': 'Software Engineering', 'year': 1, 'name': 'Discrete Mathematics'},
            {'program': 'Software Engineering', 'year': 1, 'name': 'Computer Fundamentals'},
            {'program': 'Software Engineering', 'year': 1, 'name': 'Communication Skills'},
            {'program': 'Software Engineering', 'year': 2, 'name': 'Data Structures and Algorithms'},
            {'program': 'Software Engineering', 'year': 2, 'name': 'Database Systems'},
            {'program': 'Software Engineering', 'year': 2, 'name': 'Object-Oriented Programming'},
            {'program': 'Software Engineering', 'year': 2, 'name': 'Computer Networks'},
            {'program': 'Software Engineering', 'year': 3, 'name': 'Software Engineering'},
            {'program': 'Software Engineering', 'year': 3, 'name': 'Operating Systems'},
            {'program': 'Software Engineering', 'year': 3, 'name': 'Web Development'},
            {'program': 'Software Engineering', 'year': 3, 'name': 'Mobile Application Development'},
            {'program': 'Software Engineering', 'year': 4, 'name': 'Artificial Intelligence'},
            {'program': 'Software Engineering', 'year': 4, 'name': 'Cloud Computing'},
            {'program': 'Software Engineering', 'year': 4, 'name': 'Big Data Analytics'},
            {'program': 'Software Engineering', 'year': 4, 'name': 'Project Management'},
        ]

        # Create records
        for student in students:
            Student.objects.create(**student)

        for subject in subjects:
            Subject.objects.create(**subject)

        self.stdout.write(self.style.SUCCESS('Successfully loaded initial data'))