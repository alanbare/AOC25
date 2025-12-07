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

def solve(lines, row) -> int:
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


with open('Day 7/data.txt') as f:
    lines = f.read().splitlines()
    rows = len(lines)
    splits = 0

    grid = [list(line) for line in lines]

    for r in range(rows):
        splits += solve(grid, r)

    print(f"Sum is: {splits}")