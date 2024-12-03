from collections import Counter

def read_input(file_path):
    left_list = []
    right_list = []
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    return left_list, right_list

# calculate similarity score
def calculate_similarity_score(left_list, right_list):
    right_list_count = Counter(right_list)
    similarity_score = sum(left_num * right_list_count[left_num] for left_num in left_list)
    
    return similarity_score

def main():
    file_path = 'data.txt'
    left_list, right_list = read_input(file_path)
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f"Similarity Score: {similarity_score}")

if __name__ == '__main__':
    main()
