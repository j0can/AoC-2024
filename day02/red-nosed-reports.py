def is_safe(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    
    if all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences):
        return all(1 <= abs(diff) <= 3 for diff in differences)
    
    return False


def is_safe_with_dampener(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True
    
    return False


def count_safe_reports_with_dampener(file_path):
    safe_count = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe_with_dampener(report):
                safe_count += 1
    
    return safe_count


file_path = 'reports.txt'
result = count_safe_reports_with_dampener(file_path)
print(f"Number of safe reports with Problem Dampener: {result}")
