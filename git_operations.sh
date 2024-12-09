#!/bin/bash

# Load configuration
CONFIG_FILE=".git_operations_config"
if [ -f "$CONFIG_FILE" ]; then
    source "$CONFIG_FILE"
fi

YEAR=${YEAR:-2024}
DEFAULT_BRANCH=${DEFAULT_BRANCH:-master}
BRANCH=$DEFAULT_BRANCH
PULL_BEFORE_PUSH=false

# Display instructions
if [[ "$1" == "--help" ]]; then
    echo "Usage: ./git_operations.sh <day_number> [custom_commit_message] [-b:branchname] [-pbp]"
    echo "Options:"
    echo "  -b:branchname    Specify the branch to push to (default is '$DEFAULT_BRANCH' , master)."
    echo "  -pbp             Pull latest changes from the branch before pushing."
    echo "  --help           Display this help message."
    exit 0
fi

# Parse arguments
DAY_NUMBER=$1
COMMIT_MESSAGE=${2:-"Add or update code for day $DAY_NUMBER of $YEAR"}
for arg in "$@"; do
    case $arg in
        -b:*)
            BRANCH="${arg#-b:}"
            ;;
        -pbp)
            PULL_BEFORE_PUSH=true
            ;;
    esac
done

# Validate day number
if [ -z "$DAY_NUMBER" ]; then
    echo "Error: Please provide a day number as an argument."
    echo "Usage: ./git_operations.sh <day_number> [custom_commit_message] [-b:branchname] [-pbp]"
    exit 1
fi

DAY_FOLDER="$YEAR/d$DAY_NUMBER"
if [ ! -d "$DAY_FOLDER" ]; then
    echo "Error: The folder for day $DAY_NUMBER does not exist. Please create it before running the script."
    exit 1
fi

# Function: Log actions to a file
log_action() {
    LOG_FILE="git_operations.log"
    echo "[$(date)] $1" >>"$LOG_FILE"
}

# Function: Validate code quality
validate_code() {
    echo "Running linting checks..."
    if command -v pylint &>/dev/null; then
        pylint "$DAY_FOLDER"/*.py || {
            echo "Linting failed. Fix issues before committing."
            exit 1
        }
    else
        echo "pylint not found. Skipping linting checks."
    fi
}

# Show git status and confirm
echo "Changes to be committed:"
git status
read -p "Do you want to continue? (y/n): " confirm
if [[ "$confirm" != "y" ]]; then
    echo "Commit aborted."
    exit 1
fi

# Pull latest changes if requested
if $PULL_BEFORE_PUSH; then
    echo "Pulling latest changes from branch '$BRANCH'..."
    git pull origin "$BRANCH" || {
        echo "Pull failed. Resolve conflicts and try again."
        exit 1
    }
fi

# Stage, commit, and push changes
echo "Staging changes..."
git add .

validate_code

echo "Committing changes..."
git commit -m "$COMMIT_MESSAGE" || {
    echo "Commit failed. Resolve issues and try again."
    exit 1
}

echo "Pushing changes to branch '$BRANCH'..."
git push origin "$BRANCH" || {
    echo "Push failed. Resolve issues and try again."
    exit 1
}

# Post-action notification
if command -v notify-send &>/dev/null; then
    notify-send "Git Operations" "Day $DAY_NUMBER changes committed and pushed to $BRANCH successfully!"
fi

log_action "Day $DAY_NUMBER changes committed with message: '$COMMIT_MESSAGE' and pushed to branch '$BRANCH'."

echo "Done! Day $DAY_NUMBER changes have been committed and pushed."

