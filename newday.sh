#!/bin/bash

# Usage: ./get_input.sh --day 1
# You must fill in SESSION following the instructions below.
# DO NOT run this in a loop, just once.

# You can find SESSION by using Chrome tools:
# 1) Go to https://adventofcode.com/2024/day/1/input
# 2) right-click -> inspect -> click the "Application" tab.
# 3) Refresh
# 5) Click https://adventofcode.com under "Cookies"
# 6) Grab the value for session. Fill it in.
SESSION="<FILL_ME_IN>"

USERAGENT="https://github.com/OWAIS-KHAWAJA-789/advent_of_code by owaiskhawaja789@gmail.com"

# Default value for year (hardcoded as 2022)
YEAR=2024

# Ensure that the day argument is passed and valid
if [[ $# -ne 2 || "$1" != "--day" || ! "$2" =~ ^[0-9]+$ ]]; then
  echo "Usage: $0 --day <day>"
  exit 1
fi

DAY="$2"

# Construct the URL to fetch the input
URL="https://adventofcode.com/$YEAR/day/$DAY/input"

# Fetch the input using curl
OUTPUT=$(curl -s -X GET "$URL" --cookie "session=$SESSION" -A "$USERAGENT")

# Create a directory for the day (e.g., d1, d2, ...)
DIR="d$DAY"
mkdir -p "$DIR"

# Save the output to input.txt in the created directory
echo "$OUTPUT" > "$DIR/input.txt"

# Print the first 10 lines of the output to stderr
echo "$OUTPUT" | head -n 10 >&2

echo "Input saved in $DIR/input.txt"

