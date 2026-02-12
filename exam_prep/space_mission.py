
n = int(input())
field = [input().split() for x in range(n)]
ship_start = []
fuel = 100

for row in range(n):
    for col in range(n):
        if field[row][col] == "S":
            ship_start = [row, col]
field[ship_start[0]][ship_start[1]] = '.'


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()
    move_row, move_col = directions[command]
    fuel -= 5

    next_row = ship_start[0] + move_row
    next_col = ship_start[1] + move_col

    if not (0 <= next_row < n and 0 <= next_col <n):
        print("Mission failed! The spaceship was lost in space.")
        field[ship_start[0]][ship_start[1]] = "S"
        break

    ship_start = [next_row, next_col]
    symbol = field[next_row][next_col]

    if symbol == "P":
        print(f"Mission accomplished! The spaceship reached Planet B with {fuel} resources left.")
        break
    elif symbol == "M":
        fuel -= 5
        field[next_row][next_col] = "."
    elif symbol == "R":
        fuel += 10
        if fuel > 100:
            fuel = 100

    if fuel < 5:
        print(f"Mission failed! The spaceship was stranded in space.")
        field[ship_start[0]][ship_start[1]] = "S"
        break

for row in field:
    print(*row)




