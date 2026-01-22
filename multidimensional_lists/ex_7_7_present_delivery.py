presents_number = int(input())
matrix_size = int(input())

matrix = []
santa = []
nice_kids = 0


for row in range(matrix_size):
    matrix.append(input().split())
    for col in range(matrix_size):
        if matrix[row][col] == "S":
            santa = [row, col]
        if matrix[row][col] == "V":
            nice_kids += 1

initial_kids = nice_kids

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),}

while True:
    command = input()
    if command == "Christmas morning":
        break

    new_row = santa[0] + directions[command][0]
    new_col = santa[1] + directions[command][1]

    if 0 <= new_row < matrix_size and 0 <= new_col < matrix_size:
        matrix[santa[0]][santa[1]] = "-"
        santa = [new_row, new_col]
        if matrix[new_row][new_col] == "V":
            nice_kids -= 1
            presents_number -= 1
        elif matrix[new_row][new_col] == "C":
            for move_name, move_coords in directions.items():
                if presents_number == 0:
                    break

                n_row = new_row + move_coords[0]
                n_col = new_col + move_coords[1]

                if matrix[n_row][n_col] == "V":
                    nice_kids -= 1
                    presents_number -= 1
                    matrix[n_row][n_col] = "-"
                elif matrix[n_row][n_col] == "X":
                    presents_number -= 1
                    matrix[n_row][n_col] = "-"
        matrix[new_row][new_col] = "S"

    if presents_number == 0:
        if nice_kids > 0:
            print("Santa ran out of presents!")
        break

[print(*row) for row in matrix]

if nice_kids == 0:
    print(f"Good job, Santa! {initial_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")