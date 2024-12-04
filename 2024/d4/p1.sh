#!/bin/bash

filename="input.txt"
if [ ! -f "$filename" ]; then
    echo "File '$filename' does not exist."
    exit 1
fi

map=()
while IFS= read -r line; do
    map+=("$line")
done < "$filename"

rows=${#map[@]}
cols=${#map[0]}
dirs=(
    "0 1"   # right
    "1 0"   # down
    "0 -1"  # left
    "-1 0"  # up
    "1 1"   # down-right diagonal
    "1 -1"  # down-left diag
    "-1 1"  # up-right diag
    "-1 -1" # up-left diag
)

count=0

for ((y = 0; y < rows; y++)); do
    for ((x = 0; x < cols; x++)); do
        if [ "${map[$y]:$x:1}" == "X" ]; then
            for dir in "${dirs[@]}"; do
                read -r dy dx <<< "$dir"
                if ((y + 3 * dy >= 0 && y + 3 * dy < rows && x + 3 * dx >= 0 && x + 3 * dx < cols)); then
                    if [ "${map[$y]:$x:1}" == "X" ] &&
                       [ "${map[$((y + dy))]:$((x + dx)):1}" == "M" ] &&
                       [ "${map[$((y + 2 * dy))]:$((x + 2 * dx)):1}" == "A" ] &&
                       [ "${map[$((y + 3 * dy))]:$((x + 3 * dx)):1}" == "S" ]; then
                        count=$((count + 1))
                    fi
                fi
            done
        fi
    done
done
echo "$count"
