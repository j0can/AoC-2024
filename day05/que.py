from collections import defaultdict, deque

def parse_input_from_file(file_path):
    with open(file_path, 'r') as f:
        input_text = f.read()
    rules_section, updates_section = input_text.strip().split("\n\n")
    
    rules = []
    for line in rules_section.splitlines():
        x, y = map(int, line.split('|'))
        rules.append((x, y))
    
    updates = [list(map(int, update.split(','))) for update in updates_section.splitlines()]
    
    return rules, updates

def build_graph(rules):
    graph = {}
    for x, y in rules:
        if x not in graph:
            graph[x] = []
        graph[x].append(y)
    return graph

def is_valid_update(update, graph):
    index_map = {page: i for i, page in enumerate(update)}
    for x in graph:
        for y in graph[x]:
            if x in index_map and y in index_map:
                if index_map[x] > index_map[y]:
                    return False
    return True

def find_middle_page(update):
    return update[len(update) // 2]

def solve_from_file(file_path):
    rules, updates = parse_input_from_file(file_path)
    
    graph = build_graph(rules)
    total_middle_sum = 0
    for update in updates:
        if is_valid_update(update, graph):
            total_middle_sum += find_middle_page(update)
    
    return total_middle_sum

file_path = 'values.txt'
result = solve_from_file(file_path)
print(result)

def reorder_update(update, graph):
    adj_list = defaultdict(list)
    in_degree = defaultdict(int)

    update_set = set(update)
    for x in graph:
        for y in graph[x]:
            if x in update_set and y in update_set:
                adj_list[x].append(y)
                in_degree[y] += 1
                if x not in in_degree:
                    in_degree[x] = 0

    sorted_update = []
    zero_in_degree = deque([node for node in update if in_degree[node] == 0])

    while zero_in_degree:
        node = zero_in_degree.popleft()
        sorted_update.append(node)
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)

    return sorted_update

def solve_part_two(file_path):
    rules, updates = parse_input_from_file(file_path)

    graph = build_graph(rules)

    total_middle_sum = 0
    for update in updates:
        if not is_valid_update(update, graph):
            reordered_update = reorder_update(update, graph)
            total_middle_sum += find_middle_page(reordered_update)
    
    return total_middle_sum

file_path = 'values.txt'

result = solve_part_two(file_path)
print(result)
