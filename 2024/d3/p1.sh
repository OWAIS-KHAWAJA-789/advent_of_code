#!/bin/bash


is_valid_multiplication() {
    local expr="$1"
    
    
    if [[ "$expr" =~ ^[0-9]+(\*[0-9]+)+$ ]]; then
        return 0  
    else
        return 1  
    fi
}


inputs=("5*5" "10*20" "30*3" "abc*xyz" "15*15*2")


total_sum=0


for input in "${inputs[@]}"; do
    if is_valid_multiplication "$input"; then
        
        IFS="*" read -r -a numbers <<< "$input"

        
        product=1

        
        for number in "${numbers[@]}"; do
            product=$((product * number))
        done

        
        total_sum=$((total_sum + product))
    fi
done


echo "Total sum of valid multiplications: $total_sum"
