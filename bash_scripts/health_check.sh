#!/bin/bash

# Define log file
LOG_FILE="/var/log/server_health.log"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

# Create log directory if it doesn't exist
mkdir -p "$(dirname "$LOG_FILE")"

# Function to log messages
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# Function to check resource usage
check_resources() {
    log "Checking server resources..."
    
    # Check CPU usage
    CPU_USAGE=$(top -bn1 | awk '/Cpu\(s\)/ {print 100 - $8}')
    log "CPU Usage: ${CPU_USAGE}%"
    
    # Check Memory usage
    MEM_USAGE=$(free | awk '/Mem/ {printf "%.1f", $3/$2 * 100.0}')
    log "Memory Usage: ${MEM_USAGE}%"
    
    # Check Disk space
    DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}' | tr -d '%')
    log "Disk Usage: ${DISK_USAGE}%"
    
    # Check if web server is running
    if systemctl is-active --quiet nginx || systemctl is-active --quiet apache2; then
        log "Web server is running"
    else
        log "WARNING: Web server is not running!"
    fi
    
    # Check if resources are critical
    if (( $(echo "$CPU_USAGE > 80" | bc -l) )); then
        log "WARNING: High CPU usage detected!"
    fi
    
    if (( $(echo "$MEM_USAGE > 80" | bc -l) )); then
        log "WARNING: High memory usage detected!"
    fi
    
    if [ "$DISK_USAGE" -gt 90 ]; then
        log "CRITICAL: Disk space is critically low!"
    fi
}

# Function to check API endpoints
check_api() {
    local endpoints=("/api/students" "/api/subjects")
    local base_url="http://localhost"  # Changed to localhost for security
    
    log "Checking API endpoints..."
    
    for endpoint in "${endpoints[@]}"; do
        status_code=$(curl -s -o /dev/null -w "%{http_code}" "${base_url}${endpoint}")
        
        if [ "$status_code" -eq 200 ]; then
            log "Endpoint ${endpoint} is working (Status: ${status_code})"
        else
            log "WARNING: Endpoint ${endpoint} is not responding (Status: ${status_code})"
        fi
    done
}

# Main execution
log "Starting health check..."
check_resources
check_api
log "Health check completed"