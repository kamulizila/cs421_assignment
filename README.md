# CS 421 Assignment 1 - Build and Deploy a Simple API

This repository contains a Django REST API that provides student and subject information for the CS 421 assignment.

## API Endpoints

1. `http://ec2-54-175-59-76.compute-1.amazonaws.com/api/students/` - Returns a list of 10 students with their names and enrolled programs.
2. `http://ec2-54-175-59-76.compute-1.amazonaws.com/api/subjects/` - Returns all subjects for the Software Engineering program grouped by academic year.

## Requirements
1. `pytest==7.4.0`
2. `black==23.12.0`
3. `django-debug-toolbar==4.2.0`
4. `Django==4.2.0`
5. `djangorestframework==3.14.0`
6. `psycopg2==2.9.6` (PostgreSQL adapter for Python)

### Prerequisites

- Python 3.8 or higher
- PostgreSQL database
- Virtual environment (optional but recommended)

### Installation
python3 -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
pip install pytest==7.4.0 black==23.12.0 django-debug-toolbar==4.2.0 djangorestframework==3.14.0 psycopg2==2.9.6
sudo apt update
sudo apt install postgresql postgresql-contrib

#### Step 1: Clone the repository

Clone the repository from GitHub to the local machine or server:

```bash
git clone https://github.com/kamulizila/cs421_assignment.git
cd cs421_assignment
