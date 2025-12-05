def solve(ranges, ids):
    total = 0
    for id in ids:
        for m_range in ranges:
            values = m_range.split("-")
            start = int(values[0])
            end = int(values[1])

            if start <= id <= end:
                total += 1
                break
    return total


with open('Day 5/data.txt') as f:
    lines = f.readlines()
    ranges = []
    ids = []
    switch = False
    for line in lines:
        line = line.strip()
        if line == "":
            switch = True
            continue
        if not switch:
            ranges.append(line)
        else:
            ids.append(int(line))

    sum = solve(ranges, ids)
    print("Sum is:", sum)
