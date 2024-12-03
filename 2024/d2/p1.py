def is_safe(report):
    # Check length of report
    if len(report) < 2:
        return True  # A report with one number is safe

    # Check diffrncs between adjacent numbers
    differences = [report[i+1] - report[i] for i in range(len(report)-1)]

    # Check if report is either increasing decreasing
    is_increasing = all(diff > 0 for diff in differences)
    is_decreasing = all(diff < 0 for diff in differences)

    # Check if all differences are between 1 and 3
    all_differences_valid = all(1 <= abs(diff) <= 3 for diff in differences)

    return (is_increasing or is_decreasing) and all_differences_valid

def count_safe_reports(data):
    safe_count = 0
    for report in data:
        if is_safe(report):
            safe_count += 1
    return safe_count

def read_data_from_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            # Convert each line to a list of integers
            report = list(map(int, line.strip().split()))
            data.append(report)
    return data

input_file_path = 'input.txt'
data = read_data_from_file(input_file_path)
safe_reports_count = count_safe_reports(data)
print(f"Number of safe reports: {safe_reports_count}")
