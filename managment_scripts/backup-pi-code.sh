#!/bin/bash

# Define the folder to push
directory="/home/val/github/pixel-bytes/"
log_file="/home/val/github-backup-logs.txt"

# Write date and time to log file
echo "Backup run at: $(date)" >> "$log_file"

# Navigate to the folder
cd "$directory" || {
  echo "Failed to navigate to directory: $directory" >> "$log_file"
  exit 1
}

# Make sure the folder is connected to GitHub and using the correct branch
if [ ! -d ".git" ]; then
  echo "This directory is not a Git repository. Please clone the repository first." >> "$log_file"
  exit 1
fi

# Checkout the correct branch
git checkout pi-code-backup >> "$log_file" 2>&1 || {
  echo "Failed to checkout branch pi-code-backup." >> "$log_file"
  exit 1
}

# Check if there are any changes to add
if [ -z "$(git status --porcelain)" ]; then
  echo "No changes to commit. Exiting." >> "$log_file"
  exit 0
fi

# Add all changes to staging
git add . >> "$log_file" 2>&1

# Commit the changes with a generic message
git commit -m "Automated commit at $(date)" >> "$log_file" 2>&1

# Push the changes to GitHub
git push origin pi-code-backup >> "$log_file" 2>&1 || {
  echo "Failed to push changes." >> "$log_file"
  exit 1
}

# Log success message
echo "Successfully pushed changes to GitHub." >> "$log_file"

# Exit the script
exit 0
