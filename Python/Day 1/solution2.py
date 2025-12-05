def get_position(input: str, curr_position: int):
    left = input[0] == 'L'
    rotation = int(input[1:])

    if left:
        rotation = -rotation

    crossed_zero = 0

    if rotation > 100 or rotation < -100:
        crossed_zero += abs(rotation) // 100    # full rotation every 100
        rotation = rotation % 100
        if left:
            rotation -= 100 # because I really just want the remainder not circle index

    # compare if we crossed zero
    normal_rotation = curr_position + rotation
    new_position = (curr_position + rotation) % 100

    if (normal_rotation != new_position or new_position == 0) and curr_position != 0:
        crossed_zero += 1

    return new_position, crossed_zero

def solve(lines: list[str]) -> int:
    position = 50
    crossed_zero = 0
    for line in lines:
        line = line.strip()
        position, crossed_zeros = get_position(line, position)
        crossed_zero += crossed_zeros
    return crossed_zero


with open("Day 1/data.txt", "r") as file:
    lines = file.readlines()
    crossed_zero = solve(lines)
    print(f"Croseed zero {crossed_zero} times.")
