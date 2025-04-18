#!/bin/bash 

# Define variables
LOG_FILE="/home/ubuntu/cs421_assignment/logs/backup.log"
BACKUP_DIR="/home/ubuntu/backups"
API_DIR="/home/ubuntu/cs421_assignment"
DB_USER="postgres"
DB_NAME="api_db"

# Create directories if they don't exist
mkdir -p "$BACKUP_DIR"
mkdir -p "$(dirname "$LOG_FILE")"

# Function to log messages
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

log "Starting backup process..."

# Validate API directory exists
if [ ! -d "$API_DIR" ]; then
    log "ERROR: API directory $API_DIR does not exist"
    exit 1
fi

# Backup API directory
API_BACKUP_FILE="$BACKUP_DIR/api_backup_$(date +%F).tar.gz"
if tar -czf "$API_BACKUP_FILE" -C "$(dirname "$API_DIR")" "$(basename "$API_DIR")" 2>> "$LOG_FILE"; then
    log "API backup created: $API_BACKUP_FILE"
else
    log "ERROR: Failed to create API backup"
    exit 1
fi

# Backup database (PostgreSQL)
DB_BACKUP_FILE="$BACKUP_DIR/db_backup_$(date +%F).sql"
if command -v pg_dump >/dev/null 2>&1; then
    # Read password securely
    read -s -p "Enter PostgreSQL password for $DB_USER: " DB_PASS
    echo
    
    if PGPASSWORD="$DB_PASS" pg_dump -U "$DB_USER" -d "$DB_NAME" > "$DB_BACKUP_FILE" 2>> "$LOG_FILE"; then
        log "Database backup created: $DB_BACKUP_FILE"
    else
        log "WARNING: Failed to create database backup (check credentials or connection)"
    fi

    # Clear the password variable
    unset DB_PASS
else
    log "WARNING: pg_dump not found. Skipping database backup."
fi

# Clean up old backups (older than 7 days)
find "$BACKUP_DIR" -name "api_backup_*.tar.gz" -mtime +7 -delete 2>> "$LOG_FILE"
find "$BACKUP_DIR" -name "db_backup_*.sql" -mtime +7 -delete 2>> "$LOG_FILE"
log "Deleted backups older than 7 days"

log "Backup process completed successfully"
