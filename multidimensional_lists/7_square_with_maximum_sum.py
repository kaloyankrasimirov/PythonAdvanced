rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    data = [int(el) for el in input().split(", ")]
    matrix.append(data)

max_sum = float("-inf")
sub_matrix = []

for row_index in range(rows -1):
    for col_index in range(cols -1):
        current_el = matrix[row_index][col_index]
        next_el = matrix[row_index][col_index +1]
        el_below = matrix[row_index +1][col_index]
        el_diagonal = matrix[row_index +1][col_index +1]
        sum_el = current_el + next_el + el_diagonal + el_below
        if sum_el > max_sum:
            max_sum = sum_el
            sub_matrix = [
                [current_el, next_el],
                [el_below, el_diagonal]
            ]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)