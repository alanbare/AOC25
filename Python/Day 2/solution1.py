def solve(input: str):
    sum = 0
    for m_range in input.split(","):
        values = m_range.split("-")
        start = int(values[0])
        end = int(values[1])

        for num in range(start, end + 1):
            str_num = str(num)
            if len(str_num) % 2 != 0:
                continue
            mid = len(str_num) // 2
            first_half = str_num[:mid]
            second_half = str_num[mid:]
            if first_half == second_half:
                sum += num
    return sum


with open('Day 2/data.txt') as f:
    lines = f.readlines()
    sum = solve(lines[0])
    print("Sum is:", sum)
