def move_guard(grid, obstruction_x, obstruction_y):
    # Direction vectors for up, right, down, left
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    # Turn right mapping: ^ -> >, > -> v, v -> <, < -> ^
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    
    # Find the initial guard position and direction
    rows = len(grid)
    cols = len(grid[0])
    
    start_x, start_y, direction = None, None, None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in directions:
                start_x, start_y = r, c
                direction = grid[r][c]
                break
        if start_x is not None:
            break
    
    # Set to track visited positions and direction states (x, y, direction)
    visited = set()
    visited.add((start_x, start_y, direction))
    
    # Simulate the movement
    x, y = start_x, start_y
    while True:
        # Check if next step is valid
        dx, dy = directions[direction]
        new_x, new_y = x + dx, y + dy
        
        # If the next position is out of bounds, stop
        if not (0 <= new_x < rows and 0 <= new_y < cols):
            break
        
        # If the next position is an obstacle (including the added one), turn right
        if (new_x == obstruction_x and new_y == obstruction_y) or grid[new_x][new_y] == '#':
            direction = turn_right[direction]
        else:
            # Move to the new position
            x, y = new_x, new_y
            if (x, y, direction) in visited:
                # The guard gets stuck in a loop
                return True
            visited.add((x, y, direction))
    
    return False

def read_input(filename):
    # Read the grid from the input file
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return grid

def find_possible_obstructions(grid):
    rows = len(grid)
    cols = len(grid[0])
    possible_positions = 0
    
    # First, simulate the guard's movement and get the visited positions
    visited_positions = set()
    start_x, start_y, direction = None, None, None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in {'^', 'v', '<', '>'}:
                start_x, start_y = r, c
                direction = grid[r][c]
                break
        if start_x is not None:
            break
    
    # Simulate the guard's movement without any new obstruction
    x, y = start_x, start_y
    visited_positions.add((x, y, direction))
    
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    
    while True:
        dx, dy = directions[direction]
        new_x, new_y = x + dx, y + dy
        
        if not (0 <= new_x < rows and 0 <= new_y < cols):
            break
        
        if grid[new_x][new_y] == '#' or (new_x == start_x and new_y == start_y):
            direction = turn_right[direction]
        else:
            x, y = new_x, new_y
            if (x, y, direction) in visited_positions:
                break
            visited_positions.add((x, y, direction))

    # Now check every empty space for potential obstruction
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.' and (r != start_x or c != start_y):  # Skip the starting position
                if move_guard(grid, r, c):
                    possible_positions += 1
    
    return possible_positions

# Read the input from 'input.txt'
grid = read_input('input.txt')

# Output the result
print(find_possible_obstructions(grid))

