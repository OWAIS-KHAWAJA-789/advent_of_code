def move_guard(grid):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    
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
    visited = set()
    visited.add((start_x, start_y))
    
    x, y = start_x, start_y
    while True:
        dx, dy = directions[direction]
        new_x, new_y = x + dx, y + dy
        
        if not (0 <= new_x < rows and 0 <= new_y < cols):
            break
        
        if grid[new_x][new_y] == '#':
            direction = turn_right[direction]
        else:
            x, y = new_x, new_y
            visited.add((x, y))
    
    return len(visited)

def read_input(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return grid
grid = read_input('input.txt')
print(move_guard(grid))

