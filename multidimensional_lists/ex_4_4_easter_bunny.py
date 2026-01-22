n = int(input())

field = []
bunny = []

for row in range(n):
    field.append(input().split())
    for col in range(n):
        if field[row][col] == "B":
            bunny = [row, col]

possible_moves = {
    "down": (1, 0),
    "up": (-1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
collected_eggs = float("-inf")
max_direction = ""
max_mat = []

for direction, move in possible_moves.items():
    eggs = 0
    current_mat = []
    row = bunny[0] + move[0]
    col = bunny[1] + move[1]

    while 0 <= row < n and 0 <= col < n:
        if field[row][col] == "X":
            break
        eggs += int(field[row][col])
        current_mat.append([row, col])
        row += move[0]
        col += move[1]

    if eggs > collected_eggs and current_mat:
        collected_eggs = eggs
        max_direction = direction
        max_mat = current_mat

print(max_direction)
[print(row) for row in max_mat]
print(collected_eggs)