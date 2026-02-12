n = int(input())
matrix = [[int(x) for x in input().split()] for row in range(n)]
bombs = [x for x in input().split()]
alive_cells = []


for bomb in bombs:
    current_bomb = bomb.split(',')
    current_bomb_row = int(current_bomb[0])
    current_bomb_col = int(current_bomb[1])
    power = matrix[current_bomb_row][current_bomb_col]
    if power > 0:
        for r in range(current_bomb_row -1, current_bomb_row +2):
            for c in range(current_bomb_col -1, current_bomb_col +2):
                if 0 <= r < n and 0 <= c < n:
                    if matrix[r][c] > 0:
                        matrix[r][c] -= power

for row in matrix:
    for cell_value in row:
        if cell_value > 0:
            alive_cells.append(cell_value)

print(f'Alive cells: {len(alive_cells)}')
print(f"Sum: {sum(alive_cells)}")
for row in matrix:
    print(*row)

