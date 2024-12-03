import re

def extract_and_sum_muls_from_file(file_path):
    with open(file_path, 'r') as file:
        corrupted_input = file.read()

    # Use regex to find all mul(x,y) patterns where x and y are nums
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, corrupted_input)
    total_sum = 0
    
    # Iterate over all matched mul(X, Y) pairs
    for match in matches:
        x, y = map(int, match)  
        total_sum += x * y  # Multiply,add to total sum
    
    return total_sum


input_file_path = 'input.txt'
result = extract_and_sum_muls_from_file(input_file_path)
print(f"Total sum of products: {result}")

