def is_safe(report):
    """Check if the report is safe (already satisfies conditions)."""
    if len(report) < 2:
        return True  # A report with one number is safe

    # Check diffrncs between adjacent numbers
    differences = [report[i+1] - report[i] for i in range(len(report)-1)]

    # Check if report is either increasing or decreasing
    is_increasing = all(diff > 0 for diff in differences)
    is_decreasing = all(diff < 0 for diff in differences)

    # Check if all differences are between 1 and 3
    all_differences_valid = all(1 <= abs(diff) <= 3 for diff in differences)

    return (is_increasing or is_decreasing) and all_differences_valid

def can_become_safe_with_one_removal(report):
    """Check if removing one element from the report makes it safe."""
    for i in range(len(report)):
        # Create new report with the i-th element removed
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

def count_safe_reports(data):
    safe_count = 0
    for report in data:
        if is_safe(report) or can_become_safe_with_one_removal(report):
            safe_count += 1
    return safe_count

def read_data_from_file(file_path):
    """Read the report data from the input file."""
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.strip().split()))
            data.append(report)
    return data

input_file_path = 'input.txt'
data = read_data_from_file(input_file_path)
safe_reports_count = count_safe_reports(data)
print(f"Number of safe reports (with Problem Dampener): {safe_reports_count}")
