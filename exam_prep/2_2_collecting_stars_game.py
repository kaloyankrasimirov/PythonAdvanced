def movement(matrix, position, direction):
    field_len = len(field)
    row, col = position
    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1

    if (row < 0 or row >= field_len or col < 0 or col >= field_len) and field[0][0] == "*":
        field[0][0] = "."
        return (0, 0), 1
    if row < 0 or row >= field_len or col < 0 or col >= field_len:
        return (0, 0), 0
    if matrix[row][col] == "#":
        return position, -1
    if matrix[row][col] == "*":
        field[row][col] = "."
        return (row, col), 1

    return (row, col), 0

n = int(input())
field = []
player = (None, None)
stars = 2

for i in range(n):
    field.append(input().split())
    for j in range(n):
        if field[i][j] == "P":
            player = (i, j)
            field[i][j] = "."

while True:
    command = input()
    player, star_change = movement(field, player, command)
    stars += star_change
    if stars >= 10:
        print(f"You won! You have collected 10 stars.")
        break

    if stars <= 0:
       print("Game over! You are out of any stars.")
       break

final_row, final_col = player
field[final_row][final_col] = "P"

print(f"Your final position is [{final_row}, {final_col}]")
for row in field:
    print(" ".join(row))