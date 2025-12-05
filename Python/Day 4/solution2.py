def get_neightbors(x: int, y: int, grid: list[list[str]]) -> bool:
    directions = [(-1, 0), (-1, 1), (-1, -1), (1, 0), (1, 1), (1, -1), (0, -1), (0, 1)]
    sum_neighbors = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] == '@' or grid[nx][ny] == '#':
                sum_neighbors += 1

    if sum_neighbors < 4:
        grid[x][y] = '#'
        return True
    return False

def solve(grid: list[list[str]]) -> int:
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                if get_neightbors(i, j, grid):
                    total += 1    
    return total

def clean_grid(grid: list[list[str]]):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '#':
                grid[row][col] = '.'


with open('Day 4/data.txt') as f:
    lines = f.readlines()
    grid = []
    for line in lines:
        grid.append(list(line.strip()))
    i = 1
    total = 0
    while True:
        free = solve(grid)
        if free == 0:
            break
        i += 1
        total += free
        clean_grid(grid)

    print("Free spaces:", total)
