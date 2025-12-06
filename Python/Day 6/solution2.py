def solve(ranges, ops, widths):
    total = 0

    # read the list column wise
    for j in range(len(ranges[0])):
        operation = ops[j]
        if operation == '+':
            row_total = 0
        else:
            row_total = 1

        numbers = []    # store all numbers in column j

        for i in range(len(ranges)):
            numbers.append(ranges[i][j])

        for k in range(widths[j]):
            num = ""
            for number in numbers:
                num += number[k]
            digit = num

            if operation == '+':
                row_total += int(digit)
            else:
                row_total *= int(digit)
        total += row_total
    return total

def find_column_widths(op_row):
    # counting real white space seperator but not counting the operation symbols cancels out except the first and last
    widths=[]
    curr_width = 0
    for i in range(len(op_row)):
        if op_row[i] in ['+', '*'] and i != 0:
            widths.append(curr_width)
            curr_width = 0
        else:
            curr_width += 1
    widths.append(curr_width+1) # last one does not have a seperator after it
    widths[0] -= 1  # first one includes the operation symbol

    ops = [p for p in op_row.strip().split(' ') if p]
    return ops, widths


with open('Day 6/data.txt') as f:
    lines = f.readlines()
    ops, widths = find_column_widths(lines[-1])

    ranges = []
    for line in lines[:-1]:
        row = []
        element = []
        i = 0
        col = 0
        while i < len(line):
            for k in range(widths[col]):
                element.append(line[i+k])
            i += widths[col] + 1    # move pointer to next element (+1 for space)
            col += 1    # move to next width description
            row.append("".join(element))
            element = []
        ranges.append(row)

    sum = solve(ranges, ops, widths)

    print ("Sum is:", sum)
