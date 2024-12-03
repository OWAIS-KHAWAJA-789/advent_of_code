import re

def find_enabled_multiplications(input_data: str) -> int:
    sum_result = 0
    enabled = True  

    
    mul_regex = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_regex = r"do\(\)"
    dont_regex = r"don't\(\)"

    
    mul_matches = list(re.finditer(mul_regex, input_data))
    do_matches = list(re.finditer(do_regex, input_data))
    dont_matches = list(re.finditer(dont_regex, input_data))

    
    all_matches = mul_matches + do_matches + dont_matches
    all_matches.sort(key=lambda m: m.start())

    for match in all_matches:
        instruction = match.group(0)

        if instruction == 'do()':
            enabled = True  
        elif instruction == "don't()":
            enabled = False  
        elif enabled and instruction.startswith('mul'):
            
            num1, num2 = map(int, match.groups())
            sum_result += num1 * num2

    return sum_result

def main():
    
    with open("input.txt", "r") as file:
        input_data = file.read()

    
    result = find_enabled_multiplications(input_data)

    print(f"Sum of enabled multiplications: {result}")

if __name__ == "__main__":
    main()
