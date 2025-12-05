def solve(input: str):
    sum = 0
    for m_range in input.split(","):
        values = m_range.split("-")
        start = int(values[0])
        end = int(values[1])

        for num in range(start, end + 1):
            str_num = str(num)
            for i in range(1, len(str_num)):
                if len(str_num) % i != 0:
                    continue
                arr = [str_num[j:j+i] for j in range(0, len(str_num), i)]
                if all(x == arr[0] for x in arr):
                    sum += num
                    break
    return sum


with open('Day 2/data.txt') as f:
    lines = f.readlines()
    sum = solve(lines[0])
    print("Sum is:", sum)
