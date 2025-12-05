def solve(m_ranges):
    intervals = []
    for m_range in m_ranges:
        values = m_range.split("-")
        start = int(values[0])
        end = int(values[1])
        interval = (start, end)
        intervals.append(interval)

    intervals.sort()    # sort intervals by left endpoint
    intervals.append("done") # need some end condition and I can do this in python lol

    i = 0
    first = intervals[i]
    second = intervals[i+1]

    START = 0
    END = 1

    L = first[START]
    R = first[END]
    total = 0
    while second != "done":
        if R < second[START]:
            # no overlap, add current inteval distance and repeat
            total += abs(L - R) + 1
            L = second[START]
            R = second[END]

        R = max(R, second[END]) # extend the interval ending if needed

        # I really would want to do first++ as these are just pointers...
        i += 1
        first = intervals[i]
        second = intervals[i+1]

    total += abs(L - R) + 1
    return total


with open('Day 5/data.txt') as f:
    lines = f.readlines()
    ranges = []
    for line in lines:
        line = line.strip()
        if line == "":
            break
        ranges.append(line)
    sum = solve(ranges)
    print("Sum is:", sum)
