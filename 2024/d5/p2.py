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

def build_constraints(rules):
    """Build a dictionary of page relationships (before or after)."""
    before = {}
    after = {}

    for x, y in rules:
        if y not in before:
            before[y] = []
        if x not in after:
            after[x] = []
        
        before[y].append(x)  
        after[x].append(y)   
    
    return before, after

def is_valid_order(update, before, after):
    """Check if the update is in valid order according to the rules."""
    positions = {page: i for i, page in enumerate(update)}
    
    
    for y, pre_pages in before.items():
        if y in positions:
            for pre in pre_pages:
                if pre in positions and positions[pre] > positions[y]:  
                    return False
    return True

def reorder_update(update, before, after):
    """Reorder the pages in the update to satisfy all constraints."""
    
    
    sorted_update = update[:]
    changed = True
    
    while changed:
        changed = False
        for i in range(len(sorted_update)):
            for j in range(i + 1, len(sorted_update)):
                page1 = sorted_update[i]
                page2 = sorted_update[j]
                
                
                if page2 in before.get(page1, []) and page1 > page2:
                    
                    sorted_update[i], sorted_update[j] = sorted_update[j], sorted_update[i]
                    changed = True
                    break
                elif page1 in after.get(page2, []) and page1 < page2:
                    
                    sorted_update[i], sorted_update[j] = sorted_update[j], sorted_update[i]
                    changed = True
                    break

    return sorted_update

def find_middle_page_number(update):
    """Return the middle page number of the update."""
    return update[len(update) // 2]

def main(file_path):
    rules, updates = parse_input(file_path)
    before, after = build_constraints(rules)

    total_middle_page_number = 0
    
    
    for update in updates:
        if not is_valid_order(update, before, after):
            
            corrected_update = reorder_update(update, before, after)
            total_middle_page_number += find_middle_page_number(corrected_update)
    
    return total_middle_page_number



file_path = 'input.txt'  
result = main(file_path)
print(result)  

