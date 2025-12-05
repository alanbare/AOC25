def solve(arr: list[int]):
    maxi = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            maxi = max(int(f"{arr[i]}{arr[j]}"), maxi)
    return maxi

with open('Day 3/data.txt') as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        arr = [int(s) for s in list(line.strip())]
        sum += solve(arr)
    print("Sum is:", sum)
