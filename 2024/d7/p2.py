import itertools


def evaluate_left_to_right(numbers, operators):
    result = numbers[0]
    for i in range(1, len(numbers)):
        if operators[i-1] == '+':
            result += numbers[i]
        elif operators[i-1] == '*':
            result *= numbers[i]
        elif operators[i-1] == '||':
            
            result = int(str(result) + str(numbers[i]))
    return result


def generate_operator_combinations(num_count):
    
    return itertools.product(['+', '*', '||'], repeat=num_count - 1)


def is_valid_equation(test_value, numbers):
    num_count = len(numbers)
    
    
    for operators in generate_operator_combinations(num_count):
        
        if evaluate_left_to_right(numbers, operators) == test_value:
            return True
    return False


def solve_puzzle(equations):
    total_calibration = 0
    
    for equation in equations:
        test_value_str, numbers_str = equation.split(": ")
        test_value = int(test_value_str)
        numbers = list(map(int, numbers_str.split()))
        
        
        if is_valid_equation(test_value, numbers):
            total_calibration += test_value
    
    return total_calibration


def read_input(filename):
    with open(filename, 'r') as file:
        equations = file.readlines()
    return equations


equations = read_input('input.txt')


result = solve_puzzle(equations)
print(result)

