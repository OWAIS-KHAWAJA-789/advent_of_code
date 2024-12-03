from collections import Counter

# Function to read the input from a file
def read_input(file_path):
    left_list = []
    right_list = []
    
    # Open the file and read line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into two numbers and convert them to integers
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    return left_list, right_list

# Function to calculate the similarity score
def calculate_similarity_score(left_list, right_list):
    # Count how often each number appears in the right list
    right_list_count = Counter(right_list)
    
    # Calculate the similarity score by summing up (number * its count in the right list)
    similarity_score = sum(left_num * right_list_count[left_num] for left_num in left_list)
    
    return similarity_score

# Main execution
def main():
    # Specify the path to the input file
    file_path = 'data.txt'  # Change this to the actual file path

    # Read the input from the file
    left_list, right_list = read_input(file_path)
    
    # Part 2: Calculate the similarity score
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f"Similarity Score: {similarity_score}")

# Call the main function to execute the program
if __name__ == '__main__':
    main()
