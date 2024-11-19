#!/bin/bash

# Variables
WEB_ROOT="/var/www/html"
BACKUP_DIR="/home/USER/backups"
MONITOR_LOG="/var/log/server_monitor.log"

# Function to backup website files and database
backup() {
    echo "Starting backup..."

    # Backup website files
    tar -czf "$BACKUP_DIR/web_backup_$(date +%Y%m%d).tar.gz" -C "$WEB_ROOT" .
    echo "Website files backed up to $BACKUP_DIR."

    # Log the backup
    echo "$(date): Backup completed" >> "$MONITOR_LOG"
}


# Function to monitor server resources
monitor_resources() {
    echo "Monitoring server resources..."

    # Get CPU usage
    CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
    # Get RAM usage
    MEM_USAGE=$(free -m | awk 'NR==2{printf "%.2f", $3*100/$2 }')
    # Get disk usage
    DISK_USAGE=$(df -h | grep '/$' | awk '{print $5}')

    # Log the resource usage
    echo "$(date): CPU Usage: $CPU_USAGE% | RAM Usage: $MEM_USAGE% | Disk Usage: $DISK_USAGE" >> "$MONITOR_LOG"
    echo "Resource usage logged to $MONITOR_LOG."
}

# Display help
show_help() {
    echo "Usage: manage_server.sh [backup|monitor_resources|all]"
    echo "Commands:"
    echo "  backup              - Backup website files and database"
    echo "  monitor_resources   - Monitor CPU, RAM, and disk usage"
    echo "  all                 - Run all tasks (backup, monitor traffic, and monitor resources)"
}

# Main script logic
case "$1" in
    backup)
        backup
        ;;
    monitor_resources)
        monitor_resources
        ;;
    all)
        backup
        monitor_resources
        ;;
    *)
        show_help
        ;;
esac
