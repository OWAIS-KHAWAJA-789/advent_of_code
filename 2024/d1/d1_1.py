def read_input(file_path):
    left_list = []
    right_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    return left_list, right_list

def calculate_distance(left_list, right_list):
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Calculate total distnc
    total_distance = sum(abs(a - b) for a, b in zip(left_list, right_list))
    
    return total_distance

def main():

    file_path = 'data.txt' 

    left_list, right_list = read_input(file_path)
    
    total_distance = calculate_distance(left_list, right_list)
    print(total_distance)
if __name__ == '__main__':
    main()

