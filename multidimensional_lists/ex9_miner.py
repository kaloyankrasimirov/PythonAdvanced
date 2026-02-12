from collections import deque

n = int(input())
command = deque(input().split())
miner = []
total_coal_on_map = 0
is_gg = False
matrix = [input().split() for x in range(n)]
for row in range(n):
    for col in range(n):
        if matrix[row][col] == "s":
            miner = [row, col]
        if matrix[row][col] == "c":
            total_coal_on_map += 1

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

gathered_coal = 0

while command:
    current_command = command.popleft()
    move_row, move_col = directions[current_command]

    next_row = miner[0] + move_row
    next_col = miner[1] + move_col

    if not (0 <= next_row < n and 0 <= next_col < n):
        miner = miner
        continue
    else:
        miner = [next_row, next_col]

    if matrix[next_row][next_col] == "e":
        print(f"Game over! ({next_row}, {next_col})")
        is_gg = True
        break

    if matrix[next_row][next_col] == "c":
        gathered_coal += 1
        miner = [next_row, next_col]
        matrix[next_row][next_col] = "*"
        if gathered_coal == total_coal_on_map:
            print(f"You collected all coal! ({miner[0]}, {miner[1]})")
            break

if gathered_coal < total_coal_on_map and not is_gg:
    print(f"{total_coal_on_map - gathered_coal} pieces of coal left. ({miner[0]}, {miner[1]})")