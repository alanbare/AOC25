def solve(ranges, ops):
    total = 0
    # read the list colum wise
    for j in range(len(ranges[0])):
        operation = ops[j]
        if operation == '+':
            row_total = 0
        else:
            row_total = 1

        for i in range(len(ranges)):
            if operation == '+':        
                row_total += int(ranges[i][j])
            else:
                row_total *= int(ranges[i][j])
        total += row_total
    return total

with open('Day 6/data.txt') as f:
    lines = f.readlines()
    ranges = []
    for line in lines:
        line = [p for p in line.strip().split(' ') if p]
        ranges.append(line)
    sum = solve(ranges[:-1], ranges[-1])
    print("Sum is:", sum)
