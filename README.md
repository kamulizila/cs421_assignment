# CS 421 Assignment 2 - Bash Scripts for Server Management

To explain different backup schemes and how each is executed, including the 
advantages and disadvantages of each.
1. Full Backup
How it works:
A full backup makes a complete copy of all data, files, and system states.
It stores everything into a backup location at once.
Advantages:
a). Easiest to restore — everything is contained in a single backup file.
b). Simple to manage and verify.

2. Incremental Backup
How it works
Backs up only the data that has changed since the last backup (either full or incremental).
The first backup is a full backup, followed by incremental backups.
Advantages:
a). Faster and uses less storage after the initial full backup.
b). Efficient for systems with frequent small changes.
c). Minimizes backup time and system load.

3.Differential Backup
How it works:
Backs up all changes made since the last full backup.
Differs from incremental backups by always comparing against the last full backup, not the last backup of any type.
Advantages:
a). Faster restores than incremental backups because only the full backup and the latest differential are needed.
b). Simpler than incremental in terms of management and recovery.
c). Good balance between backup time and storage space.

The Deployed API Endpoints from Assignment 1:

http://ec2-54-175-59-76.compute-1.amazonaws.com/api/students/ - Returns a list of 10 students with their names and enrolled programs.

http://ec2-54-175-59-76.compute-1.amazonaws.com/api/subjects/ - Returns all subjects for the Software Engineering program grouped by academic year.


Cron Job Setup

0 */6 * * * | /home/ubuntu/cs421_assignment/bash_scripts/health_check.sh -> Runs every 6 hours to log server health

0 2 * * * | /home/ubuntu/cs421_assignment/bash_scripts/backup_api.sh -> Runs daily at 2:00 AM to backup the API

0 3 */3 * * | /home/ubuntu/cs421_assignment/bash_scripts/update_server.sh -> Runs every 3 days at 3:00 AM to update packages

### Scripts Overview
1. **health_check.sh**
   - Purpose: Monitors server resources (CPU, memory, disk) and API endpoints
   - Dependencies: curl, web server (Nginx)
   - Setup: `chmod +x health_check.sh`
   - Run: `./health_check.sh`

2. **backup_api.sh**
   - Purpose: Creates backups of API files and database
   - Dependencies: tar, gzip, pg_dump (for PostgreSQL)
   - Setup: `chmod +x backup_api.sh`
   - Run: `./backup_api.sh`

3. **update_server.sh**
   - Purpose: Updates system packages and API code
   - Dependencies: git, apt
   - Setup: `chmod +x update_server.sh`
   - Run: `./update_server.sh`

   
# CS 421 Assignment 1 - Build and Deploy a Simple API

This repository contains a Django REST API that provides student and subject information for the CS 421 assignment.

## API Endpoints
http://ec2-54-175-59-76.compute-1.amazonaws.com/api/students/ - Returns a list of 10 students with their names and enrolled programs.
http://ec2-54-175-59-76.compute-1.amazonaws.com/api/subjects/ - Returns all subjects for the Software Engineering program grouped by academic year.

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
1. python3 -m venv venv
2. source venv/bin/activate 
3. pip install -r requirements.txt
4. pip install pytest==7.4.0 black==23.12.0 django-debug-toolbar==4.2.0 djangorestframework==3.14.0 psycopg2==2.9.6
5. sudo apt update
6. sudo apt install postgresql postgresql-contrib

#### Step 1: Clone the repository

Clone the repository from GitHub to the local machine or server:

```bash
git clone https://github.com/kamulizila/cs421_assignment.git
cd cs421_assignment
