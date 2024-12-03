#!/bin/bash

is_safe() {
  local report=("$@")
  local increasing=true
  local decreasing=true

  for ((i = 0; i < ${#report[@]} - 1; i++)); do
    local diff=$(( ${report[i+1]} - ${report[i]} ))
    if (( diff < 1 || diff > 3 )); then
      echo 0 
      return
    fi
    if (( ${report[i]} >= ${report[i+1]} )); then
      increasing=false
    fi
    if (( ${report[i]} <= ${report[i+1]} )); then
      decreasing=false
    fi
  done

  if $increasing || $decreasing; then
    echo 1 
  else
    echo 0 
  fi
}

is_safe_with_one_removal() {
  local report=("$@")
  local length=${#report[@]}

  for ((i = 0; i < $length; i++)); do
    local new_report=("${report[@]:0:$i}" "${report[@]:$((i + 1))}")
    if [[ $(is_safe "${new_report[@]}") -eq 1 ]]; then
      echo 1  
      return
    fi
  done

  echo 0  
}

process_reports() {
  local input_file=$1
  local safe_reports_part1=0
  local safe_reports_part2=0

  while IFS= read -r line; do
    report=($line)

    if [[ $(is_safe "${report[@]}") -eq 1 ]]; then
      ((safe_reports_part1++))
    fi

    if [[ $(is_safe_with_one_removal "${report[@]}") -eq 1 ]]; then
      ((safe_reports_part2++))
    fi
  done < "$input_file"

  echo "Part 1 - Safe Reports: $safe_reports_part1"
  echo "Part 2 - Safe Reports with One Removal: $safe_reports_part2"
}

process_reports "input.txt"
