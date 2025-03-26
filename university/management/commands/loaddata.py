from django.core.management.base import BaseCommand
from university.models import Student, Subject

class Command(BaseCommand):
    help = 'Load initial data into database'

    def handle(self, *args, **options):
        # Students data
        students = [
            {'name': 'Kamuli zila', 'program': 'Software Engineering'},
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
            {'program': 'Software Engineering', 'year': 1, 'name': 'Principles of Programming Languages (CP 111)'},
            {'program': 'Software Engineering', 'year': 1, 'name': 'Development Perspectives (DS 102)'},
            {'program': 'Software Engineering', 'year': 1, 'name': 'Mathematical Foundations of Information Security (IA 112)'},
            {'program': 'Software Engineering', 'year': 1, 'name': 'Introduction to Information Technology (IT 111)'},
            {'program': 'Software Engineering', 'year': 1, 'name': 'Communication Skills (LG 102)'},
            {'program': 'Software Engineering', 'year': 1, 'name': 'Discrete Mathematics for ICT (MT 1111)'},
            {'program': 'Software Engineering', 'year': 1, 'name': 'Calculus (MT 1112)'},
            {'program': 'Software Engineering', 'year': 1, 'name': 'Linear Algebra for ICT (MT 1117)'},
            {'program': 'Software Engineering', 'year': 1, 'name': 'CN 121-Introduction to Computer Networking'},
            {'program': 'Software Engineering', 'year': 1, 'name': 'CP 121-Introduction to Database systems'},
            {'program': 'Software Engineering', 'year': 1, 'name': 'CP 123-Introduction to High Level Programming'},
            {'program': 'Software Engineering', 'year': 1, 'name': 'CS 123-Introduction to Software Engineering'},
            {'program': 'Software Engineering', 'year': 1, 'name': 'IA 124-Introduction to IT Security'},
            {'program': 'Software Engineering', 'year': 1, 'name': 'MT 1211-Numerical Analysis for ICT'},
            {'program': 'Software Engineering', 'year': 1, 'name': 'ST 1210-Introduction to Probability and Statistics'},

            {'program': 'Software Engineering', 'year': 2, 'name': 'CN 211-Computer Networking Protocols'},
            {'program': 'Software Engineering', 'year': 2, 'name': 'CP 211-Introduction To Linux/Unix Systems'},
            {'program': 'Software Engineering', 'year': 2, 'name': 'CP 212-Systems Analysis and Design'},
            {'program': 'Software Engineering', 'year': 2, 'name': 'CP 213-Data Structures and Algorithms Analysis'},
            {'program': 'Software Engineering', 'year': 2, 'name': 'CP 214-Computational Theory'},
            {'program': 'Software Engineering', 'year': 2, 'name': 'CP 215-Object Oriented Programming in Java'},
            {'program': 'Software Engineering', 'year': 2, 'name': 'CS 131-Industrial Practical Training I'},
            {'program': 'Software Engineering', 'year': 2, 'name': 'CT 211-Computer Organization and Architecture I'},
            {'program': 'Software Engineering', 'year': 2, 'name': 'CP 221-Internet Programming And Application I'},
            {'program': 'Software Engineering', 'year': 2, 'name': 'CP 222-Open Source Technologies'},
            {'program': 'Software Engineering', 'year': 2, 'name': 'CP 223-Object-Oriented Systems Design'},
            {'program': 'Software Engineering', 'year': 2, 'name': 'CP 224-Database Management Systems'},
            {'program': 'Software Engineering', 'year': 2, 'name': 'CP 225-Software Testing and Quality Assurance'},
            {'program': 'Software Engineering', 'year': 2, 'name': 'CP 226-Operating Systems'},
            {'program': 'Software Engineering', 'year': 2, 'name': 'IS 221-ICT Research Methods'},

            {'program': 'Software Engineering', 'year': 3, 'name': 'CP 311-Internet Programming and Applications II'},
            {'program': 'Software Engineering', 'year': 3, 'name': 'CP 312-Python Programming'},
            {'program': 'Software Engineering', 'year': 3, 'name': 'CP 313-Mobile Applications Development'},
            {'program': 'Software Engineering', 'year': 3, 'name': 'CP 316-Selected Topics in Software Engineering'},
            {'program': 'Software Engineering', 'year': 3, 'name': 'CP 318-Computer Graphics'},
            {'program': 'Software Engineering', 'year': 3, 'name': 'CS 231-Industrial Practical Training II'},
            {'program': 'Software Engineering', 'year': 3, 'name': 'EME 314-ICT Entrepreneurship'},
            {'program': 'Software Engineering', 'year': 3, 'name': 'MT 3111-Mathematical Logic and Formal Semantics'},
            {'program': 'Software Engineering', 'year': 3, 'name': 'CP 321-Distributed Database Systems'},
            {'program': 'Software Engineering', 'year': 3, 'name': 'CP 322-Data Mining and Warehousing'},
            {'program': 'Software Engineering', 'year': 3, 'name': 'CP 323-Web Framework Development Using Javascript'},
            {'program': 'Software Engineering', 'year': 3, 'name': 'CP 324-Compiler Technology'},
            {'program': 'Software Engineering', 'year': 3, 'name': 'CS 321-Advanced Java Programming'},
            {'program': 'Software Engineering', 'year': 3, 'name': 'IA 321-Information and Communication Systems Security'},
            {'program': 'Software Engineering', 'year': 3, 'name': 'CP 316-Selected Topics in Software Engineering'},

            {'program': 'Software Engineering', 'year': 4, 'name': 'BT 413-ICT Project Management'},
            {'program': 'Software Engineering', 'year': 4, 'name': 'CP 314-Distributed Computing'},
            {'program': 'Software Engineering', 'year': 4, 'name': 'CP 412-C# Programming'},
            {'program': 'Software Engineering', 'year': 4, 'name': 'CS 332-Industrial Practical Training III'},
            {'program': 'Software Engineering', 'year': 4, 'name': 'CS 411-Software Reverse Engineering'},
            {'program': 'Software Engineering', 'year': 4, 'name': 'CS 431-Software Engineering Project I'},
            {'program': 'Software Engineering', 'year': 4, 'name': 'CT 312-Computer Maintenance'},
            {'program': 'Software Engineering', 'year': 4, 'name': 'IM 411-Human Computer Interaction'},
            {'program': 'Software Engineering', 'year': 4, 'name': 'SI 311-Professional Ethics and Conduct Core'},
            {'program': 'Software Engineering', 'year': 4, 'name': 'CP 329-Big Data Analysis'},
            {'program': 'Software Engineering', 'year': 4, 'name': 'CP 422-Artificial Intelligence'},
            {'program': 'Software Engineering', 'year': 4, 'name': 'CP 424-Cloud Computing'},
            {'program': 'Software Engineering', 'year': 4, 'name': 'CD 322-Digital Creative Advertising and Production'},
            {'program': 'Software Engineering', 'year': 4, 'name': 'CP 421-Digital Image Processing'},
            {'program': 'Software Engineering', 'year': 4, 'name': 'BT 321-Organizational Management'},
            {'program': 'Software Engineering', 'year': 4, 'name': 'CS 421-Software Deployment and Management'},
            {'program': 'Software Engineering', 'year': 4, 'name': 'CS 432-Software Engineering Project II'},
        ]

        # Create records
        for student in students:
            Student.objects.create(**student)

        for subject in subjects:
            Subject.objects.create(**subject)

        self.stdout.write(self.style.SUCCESS('Successfully loaded initial data'))