# CS 421 Assignment 1
#Build and deploy a simple API using your preferred programming language(Python) and relational 
database management system (Postgres).

This repository contains a Django REST API for student and subject information as required by the CS 421 assignment.

## API Endpoints

1. `http://54.175.59.76:8000/api/students/` - Returns a list of 10 students with their names and enrolled programs
2. `http://54.175.59.76:8000/api/subjects/` - Returns all subjects for the Software Engineering program grouped by academic year

## Requirements

1. pytest==7.4.0
2. black==23.12.0
3. django-debug-toolbar==4.2.0

### Prerequisites
- Python 3.8+
- SQLite (included with Python)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/kamulizila/cs421_assignment.git
   cd cs421-django-assignment
