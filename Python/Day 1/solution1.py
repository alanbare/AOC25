def get_position(input: str, curr_position: int) -> int:
    left = input[0] == 'L'
    rotation = int(input[1:])

    if left:
        rotation = -rotation

    new_position = (curr_position + rotation) % 100
    return new_position

def solve(lines: list[str]) -> None:
    position = 50
    crossed_zero = 0
    for line in lines:
        line = line.strip()
        position = get_position(line, position)
        if position == 0:
            crossed_zero += 1
    
    print(f"Croseed zero {crossed_zero} times.")


with open("Day 1/data.txt", "r") as file:
    lines = file.readlines()
    solve(lines)
