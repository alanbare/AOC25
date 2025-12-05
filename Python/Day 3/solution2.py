def LargestNumberWithNDigits(arr: list[int], left_to_take: int, starting: int, dp) -> int:
    # Returns Largest number that can be formed with left_to_take digits from arr[starting:]

    if dp[left_to_take][starting] != -1:
        return dp[left_to_take][starting]

    if left_to_take == 0:
        return 0

    for i in range(starting, len(arr)):
        # For each element in array
        # either take the element
        # or skip the element
        take = int(f"{arr[i]}{LargestNumberWithNDigits(arr, left_to_take - 1, i + 1, dp)}")
        skip = LargestNumberWithNDigits(arr, left_to_take, i + 1, dp)
        val = max(take, skip)
        dp[left_to_take][starting] = val
        return val
    return 0    # Artifical 0 as end condition

def solve(arr: list[int], line_len: int):
    n = 12
    dp = [[-1 for _ in range(line_len + 1)] for _ in range(n+1)]
    return LargestNumberWithNDigits(arr, n, 0, dp) // 10    # remove last digit added artificially


with open('Day 3/data.txt') as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        arr = [int(s) for s in list(line.strip())]
        sum += solve(arr, len(line))
    print("Sum is:", sum)
