#!/bin/bash

# Define variables
LOG_FILE="/var/log/update.log"
API_DIR="/var/www/cs421_assignment"

# Create log directory if it doesn't exist
mkdir -p "$(dirname "$LOG_FILE")"

# Function to log messages with timestamp
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# Function to check if directory exists
check_directory() {
    if [ ! -d "$1" ]; then
        log "ERROR: Directory $1 does not exist"
        exit 1
    fi
}

# Main update process
log "Starting server update process"

# Update package list
log "Updating package lists"
if ! apt update >> "$LOG_FILE" 2>&1; then
    log "ERROR: Failed to update package lists"
    exit 1
fi

# Upgrade packages
log "Upgrading system packages"
if ! apt upgrade -y >> "$LOG_FILE" 2>&1; then
    log "ERROR: Failed to upgrade packages"
    exit 1
fi
log "System packages updated successfully"

# Update API from GitHub
check_directory "$API_DIR"
log "Updating API from GitHub repository"

cd "$API_DIR" || {
    log "ERROR: Failed to change to API directory"
    exit 1
}

if ! git pull >> "$LOG_FILE" 2>&1; then
    log "ERROR: Failed to update GitHub repository"
    exit 1
fi
log "GitHub repository updated successfully"

# Restart web server
log "Attempting to restart web server"
if systemctl is-active --quiet apache2; then
    if ! systemctl restart apache2 >> "$LOG_FILE" 2>&1; then
        log "ERROR: Failed to restart Apache"
        exit 1
    fi
    log "Apache restarted successfully"
elif systemctl is-active --quiet nginx; then
    if ! systemctl restart nginx >> "$LOG_FILE" 2>&1; then
        log "ERROR: Failed to restart Nginx"
        exit 1
    fi
    log "Nginx restarted successfully"
else
    log "WARNING: No active web server (Apache or Nginx) found"
fi

log "Update process completed successfully"