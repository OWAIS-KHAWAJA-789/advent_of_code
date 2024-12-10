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
USERAGENT="https://github.com/OWAIS-KHAWAJA-789/advent_of_code/blob/master/newday.sh by owaiskhawaja789@gmail.com"
# replace with your email and identity, its just to tell AOC that who you are sending a programmed request to their server
# Ensure that the day argument is passed and valid
if [[ $# -ne 2 || "$1" != "--day" || ! "$2" =~ ^[0-9]+$ ]]; then
  echo "Usage: $0 --day <day>"
  exit 1
fi
YEAR=2024
DAY="$2"
URL="https://adventofcode.com/$YEAR/day/$DAY/input"
OUTPUT=$(curl -s -X GET "$URL" --cookie "session=$SESSION" -A "$USERAGENT")
DIR="d$DAY"
mkdir -p "advent_of_code/2024/$DIR"
echo "$OUTPUT" > "$DIR/input.txt"
echo "Input saved in $DIR/input.txt, here is df.head:"
echo "$OUTPUT" | head -n 5 >&2
