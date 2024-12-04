filename = 'input.txt'  

arr = []
with open(filename, 'r') as file:
    for line in file:
        line = line.strip()
        arr.append(line)

s = 0
for y in range(len(arr)):
    for x in range(len(arr)):
        if arr[y][x] == 'M':
            if y + 2 < len(arr) and x + 2 < len(arr[0]):
                if arr[y+1][x+1] == 'A' and arr[y+2][x+2] == 'S':
                    if (arr[y+2][x] == 'M' and arr[y][x+2] == 'S') or (arr[y+2][x] == 'S' and arr[y][x+2] == 'M'):
                        s += 1
        if arr[y][x] == 'S':
            if y + 2 < len(arr) and x + 2 < len(arr[0]):
                if arr[y+1][x+1] == 'A' and arr[y+2][x+2] == 'M':
                    if (arr[y+2][x] == 'M' and arr[y][x+2] == 'S') or (arr[y+2][x] == 'S' and arr[y][x+2] == 'M'):
                        s += 1

print(s)

