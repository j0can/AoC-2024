from collections import Counter

def total_distance_from_file(file_path):
    left_list = []
    right_list = []
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    left_list.sort()
    right_list.sort()
    
    total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))
    
    return total_distance

file_path = 'list.txt'
result = total_distance_from_file(file_path)
print(f"Total distance: {result}")

def similarity_score(file_path):
    left_list = []
    right_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    right_count = Counter(right_list)
    
    similarity = 0
    for number in left_list:
        similarity += number * right_count[number]
    
    return similarity

file_path = 'list.txt'
result = similarity_score(file_path)
print(f"Similarity score: {result}")

