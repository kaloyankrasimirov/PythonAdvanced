n_size = int(input())
matrix = []

for i in range(n_size):
    data = [int(el) for el in input().split()]
    matrix.append(data)

diagonal = 0
# for row_index in range(n_size):
#     for col_index in range(n_size):
#         if row_index == col_index:
#             diagonal += matrix[row_index][col_index]

for index in range(n_size):
    diagonal += matrix[index][index]-1


print(diagonal)