def count_xmas(grid):
    # Define word searching for
    word = "XMAS"
    word_length = len(word)
    grid_size = len(grid)
    
    # Define all 8 possible directions
    directions = [
        (0, 1),   # Horizontal: left to right
        (0, -1),  # Horizontal: right to left
        (1, 0),   # Vertical: top to bottom
        (-1, 0),  # Vertical: bottom to top
        (1, 1),   # Diagonal: top-left to bottom-right
        (-1, -1), # Diagonal: bottom-left to top-right
        (1, -1),  # Diagonal: top-right to bottom-left
        (-1, 1)   # Diagonal: bottom-right to top-left
    ]
    
    def in_bounds(x, y):
        return 0 <= x < grid_size and 0 <= y < grid_size
    
    def check_word(x, y, dx, dy):
        # Check if find "XMAS" starting at (x, y) in direction (dx, dy)
        for i in range(word_length):
            nx, ny = x + dx * i, y + dy * i
            if not in_bounds(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True
    
    count = 0
    
    # Traverse all positions 
    for i in range(grid_size):
        for j in range(grid_size):
            # Check all 8 directions from each position
            for dx, dy in directions:
                if check_word(i, j, dx, dy):
                    count += 1
    
    return count

def read_grid_from_file(filename):
    with open(filename, 'r') as f:
        # Read lines and strip any extra whitespace
        grid = [line.strip() for line in f.readlines()]
    return grid

filename = 'input.txt'

grid = read_grid_from_file(filename)
result = count_xmas(grid)
print(result)

