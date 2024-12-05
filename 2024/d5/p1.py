from collections import defaultdict

def parse_input(file_path):
    """Parse the input data from a file into two parts: rules and updates."""
    rules = []
    updates = []

    with open(file_path, 'r') as file:
        input_data = file.read().strip()

    rule_part, update_part = input_data.split("\n\n")
    
    for rule in rule_part.splitlines():
        x, y = map(int, rule.split('|'))
        rules.append((x, y))
    
    for update in update_part.splitlines():
        updates.append(list(map(int, update.split(','))))
    
    return rules, updates

def build_ordering_graph(rules):
    """Build a graph representing the ordering constraints."""
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for x, y in rules:
        graph[x].append(y)
        in_degree[y] += 1
        if x not in in_degree:
            in_degree[x] = 0
    
    return graph, in_degree

def is_valid_order(update, graph, in_degree):
    """Check if the pages in this update are in a valid order."""
    position = {page: idx for idx, page in enumerate(update)}
    
    for x, y in graph.items():
        if x in position:  
            for y_page in y:
                if y_page in position:  
                    if position[x] > position[y_page]:  
                        return False
    return True

def find_middle_page_number(update):
    """Return the middle page number of the update."""
    return update[len(update) // 2]

def main(file_path):
    rules, updates = parse_input(file_path)
    graph, in_degree = build_ordering_graph(rules)

    total_middle_page_number = 0
    
    for update in updates:
        if is_valid_order(update, graph, in_degree):
            total_middle_page_number += find_middle_page_number(update)
    
    return total_middle_page_number



file_path = 'input.txt'  
result = main(file_path)
print(result)  
