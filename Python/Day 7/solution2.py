## START PART 1 ##
def get_above(lines, row, col) -> str:
    if row == 0:
        return '.'
    if lines[row - 1][col] == 'S':
        return '|'
    return lines[row - 1][col]

def is_valid(lines, row, col) -> bool:
    if col < 0 or col >= len(lines[0]):
        return False
    if lines[row][col] != '.':
        return False
    return True

def solve1(lines, row) -> int:
    total_row = 0

    for char, _ in enumerate(lines[row]):
        current = lines[row][char]
        above = get_above(lines, row, char)
        if above == '|':
            if current == '.':
                lines[row][char] = "|"
            elif current == '^':
                found_valid = False
                if is_valid(lines, row, char - 1):
                    lines[row][char - 1] = '|'
                    found_valid = True
                if is_valid(lines, row, char + 1):
                    lines[row][char + 1] = '|'
                    found_valid = True
                if found_valid:
                    total_row += 1
    return total_row
## END PART 1 ##

def is_valid2(grid,row,col):
    if col < 0 or col >= len(grid[0]):
        return False
    if row < 0 or row >=len(grid):
        return False
    return True


# dfs with dp, O(row*col) = O(n^2)
# everytime you reach the bottom you have done so from a diffent path
def dfs(grid, row, col, dp):
    if dp[row][col] != -1:
        return dp[row][col]
    total = 0
    if is_valid2(grid, row + 1, col) and grid[row + 1][col] == '|':
        total += dfs(grid, row + 1, col, dp)
    if is_valid2(grid, row + 1, col + 1) and grid[row + 1][col] == "^" and grid[row + 1][col + 1] == '|':
        total += dfs(grid, row + 1, col + 1, dp)
    if is_valid2(grid, row + 1, col - 1) and grid[row + 1][col] == "^" and grid[row  +1][col - 1] == '|':
        total += dfs(grid, row + 1, col - 1, dp)
    if len(grid) - 1 == row:
        total += 1

    dp[row][col] = total
    return total

def solve(grid):
    col = 0
    for i, c in enumerate(grid[0]):
        if c == 'S':
            col = i
            break
    dp = [[-1 for _ in range(len(grid[0]))] for __ in range(len(grid))]
    return dfs(grid, 0, col, dp)


with open('Day 7/data.txt') as f:
    lines = f.read().splitlines()
    rows = len(lines)

    grid = [list(line) for line in lines]

    # run part 1 to get nice grid
    for r in range(rows):
        solve1(grid, r)

    sol = solve(grid)

    print(f"Sum is: {sol}")
