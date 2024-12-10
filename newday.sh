#!/bin/bash

# Usage: ./newday.sh --day 1
# You must fill in SESSION following the instructions below.
# DO NOT run this in a loop, just once.

# You can find SESSION by using Chrome tools:
# 1) Go to https://adventofcode.com/2024/day/1/input
# 2) right-click -> inspect -> click the "Application" tab.
# 3) Refresh
# 5) Click https://adventofcode.com under "Cookies"
# 6) Grab the value for session. Fill it in.

SESSION="fill_with_session_id"

USERAGENT="https://github.com/OWAIS-KHAWAJA-789/advent_of_code/blob/legacy/newday.sh by owaiskhawaja789@gmail.com"

# Ensure that the day argument is passed and valid
if [[ $# -ne 1 || ! "$1" =~ ^[0-9]+$ ]]; then
  echo "Usage: $0 <day>"
  exit 1
fi

YEAR=2024
DAY="$1"  # Take the day directly from the argument
URL="https://adventofcode.com/$YEAR/day/$DAY/input"

# Fetching input
OUTPUT=$(curl -s -X GET "$URL" --cookie "session=$SESSION" -A "$USERAGENT")

# Check if OUTPUT is empty (curl failed to get data)
if [ -z "$OUTPUT" ]; then
  echo "Failed to fetch input for day $DAY. Please check your session cookie and user agent."
  exit 2
fi

DIR="advent_of_code/2024/d$DAY"  # Folder named 'd<day>'

# Create directory structure
mkdir -p "$DIR"

# Ensure the directory was created successfully
if [ ! -d "$DIR" ]; then
  echo "Failed to create directory $DIR. Check your permissions."
  exit 3
fi

# Write the output to the file
echo "$OUTPUT" > "$DIR/input.txt"

# Ensure that the file was created
if [ ! -f "$DIR/input.txt" ]; then
  echo "Failed to create input.txt in $DIR. Check your permissions."
  exit 4
fi

echo "Input saved in $DIR/input.txt, here is the first 5 lines:"
echo "$OUTPUT" | head -n 5 >&2
