n = int(input())
matrix = []

for i in range(n):
    data = list(input())
    matrix.append(data)

symbol = input()

position = None
# is_found = False
#
# for index_row in range(n):
#     for index_col in range(n):
#         if matrix[index_row][index_col] == symbol:
#             position = (index_row, index_col)
#             is_found = True
#             break
#     if is_found:
#         break

for index_row in range(n):
    for index_col in range(n):
        if matrix[index_row][index_col] == symbol:
            position = (index_row, index_col)
            print(position)
            exit()

# if position:
#     print(position)
# else:
print(f"{symbol} does not occur in the matrix")

# print(position if position else f"{symbol} does not occur in the matrix")