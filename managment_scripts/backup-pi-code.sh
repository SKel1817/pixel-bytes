#!/bin/bash

# Define the folder to push
directory="/path/to/your/code/folder"

# Navigate to the folder
cd "$directory" || exit

# Make sure the folder is connected to GitHub and using the correct branch
if [ ! -d ".git" ]; then
  echo "This directory is not a Git repository. Please clone the repository first."
  exit 1
fi

git checkout pi-code || exit

# Add all changes to staging
git add .

# Commit the changes with a generic message
git commit -m "Automated commit at $(date)"

# Push the changes to GitHub
git push origin pi-code

# Exit the script
exit 0