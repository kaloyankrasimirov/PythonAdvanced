rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

command = input().split()

while command[0] != "END":

    action, r, c, value = command[0], int(command[1]), int(command[2]), int(command[3])

    if r < 0 or r >= rows or c < 0 or c >= len(matrix[r]):
        print("Invalid coordinates")
    else:
        if action == "Add":
            matrix[r][c] += value
        elif action == "Subtract":
                matrix[r][c] -= value

    command = input().split()

for row in matrix:
    print(*row)