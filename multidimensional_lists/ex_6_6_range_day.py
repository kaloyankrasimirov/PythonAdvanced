FIELD = 5

matrix = []
shooter = []
targets = 0


for row in range(FIELD):
    matrix.append(input().split())
    for col in range(FIELD):
        if matrix[row][col] == "A":
            shooter = [row, col]
        elif matrix[row][col] == "x":
            targets += 1

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),}
shot_targets = []

for _ in range(int(input())):
    command = input().split()
    action = command[0]
    direction = command[1]
    if action == "shoot":
        row = shooter[0] + directions[direction][0]
        col = shooter[1] + directions[direction][1]
        while 0 <= row < FIELD and 0 <= col < FIELD:
            if matrix[row][col] == "x":
                shot_targets.append([row, col])
                matrix[row][col] = "."
                targets -= 1
                break
            row += directions[direction][0]
            col += directions[direction][1]
        if targets == 0:
            print(f"Training completed! All {len(shot_targets)} targets hit.")
            break

    elif action == "move":
        steps = int(command[2])
        row = shooter[0] + directions[direction][0] * steps
        col = shooter[1] + directions[direction][1] * steps
        if 0 <= row < FIELD and 0 <= col < FIELD and matrix[row][col] == ".":
            shooter = [row, col]


if targets > 0:
    print(f"Training not completed! {targets} targets left.")

[print(row) for row in shot_targets]