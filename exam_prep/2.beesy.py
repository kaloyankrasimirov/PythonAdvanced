n = int(input())
energy = 15
energy_restored = False
minimum_nectar_needed = 30
nectar_collected = 0
bee_r = 0
bee_c = 0
matrix = []

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "B":
            bee_r, bee_c = row, col
            matrix[row][col] = "-"


def bee_movement(direction, r, c):
    if direction == "up":
        r = (r-1) % n
    if direction == "down":
        r = (r+1) % n
    if direction == "left":
        c = (c-1) % n
    if direction == "right":
        c = (c+1) % n
    return r, c

while True:
    energy -= 1
    bee_r, bee_c = bee_movement(input(), bee_r, bee_c)

    if matrix[bee_r][bee_c].isdigit():
        nectar_collected += int(matrix[bee_r][bee_c])
        matrix[bee_r][bee_c] = "-"



    if matrix[bee_r][bee_c] == "H":
        if nectar_collected >= minimum_nectar_needed:
            print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")
        break

    if energy <=0:
        if not energy_restored and nectar_collected >= minimum_nectar_needed:
            energy = nectar_collected - minimum_nectar_needed
            energy_restored = True
            nectar_collected = minimum_nectar_needed
        else:
            print("This is the end! Beesy ran out of energy.")
            break


matrix[bee_r][bee_c] = "B"
for row in matrix:
    print("".join(row))