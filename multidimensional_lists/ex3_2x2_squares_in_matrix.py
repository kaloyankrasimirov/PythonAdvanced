matrix_rows, matrix_cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(matrix_rows)]

result = 0

for row_index in range(matrix_rows -1):
    for col_index in range(matrix_cols -1):
        current_el = matrix[row_index][col_index]
        next_el = matrix[row_index][col_index +1]
        below_el = matrix[row_index +1][col_index]
        diagonal_el = matrix[row_index +1][col_index +1]

        if current_el == next_el == below_el == diagonal_el:
            result += 1

print(result)

