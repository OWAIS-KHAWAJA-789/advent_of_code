#!/bin/bash

if [ -z "$1" ]; then
    echo "Error: Please provide a day number as an argument."
    echo "Usage: ./git_operations.sh <day_number> [custom_commit_message]"
    exit 1
fi

DAY_NUMBER=$1
YEAR="2024"

DAY_FOLDER="$YEAR/d$DAY_NUMBER"
if [ ! -d "$DAY_FOLDER" ]; then
    echo "Error: The folder for day $DAY_NUMBER does not exist. Please create the folder and add your files before running the script."
    exit 1
fi

if [ -n "$2" ]; then
    COMMIT_MESSAGE="$2"
else
    COMMIT_MESSAGE="Add or update code for day $DAY_NUMBER of $YEAR"
fi
echo "Staging changes..."
git add .
echo "Committing changes..."
git commit -m "$COMMIT_MESSAGE"
echo "Pushing changes to GitHub..."
git push origin master

echo "Done! Day $DAY_NUMBER changes have been committed and pushed."

