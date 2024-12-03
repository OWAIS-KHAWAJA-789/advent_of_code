#!/bin/bash

# Check if day num is provided as argument
if [ -z "$1" ]; then
    echo "Error: Please provide a day number as an argument."
    echo "Usage: ./git_operations.sh <day_number>"
    exit 1
fi

DAY_NUMBER=$1
YEAR="2024"

# if the specific day folder exist
DAY_FOLDER="$YEAR/d$DAY_NUMBER"
if [ ! -d "$DAY_FOLDER" ]; then
    echo "Error: The folder for day $DAY_NUMBER does not exist. Please create the folder and add your files before running the script."
    exit 1
fi

# Stage all changes 
echo "Staging changes..."
git add .

# Commit changes 
echo "Committing changes..."
git commit -m "Add or update code for day $DAY_NUMBER of $YEAR"

# Push changs to github
echo "Pushing changes to GitHub..."
git push origin master

echo "Done! Day $DAY_NUMBER changes have been committed and and pushed."
