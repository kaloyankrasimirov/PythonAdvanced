n = int(input())

matrix = []
for _ in range(n):
    data = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(data)
print(matrix)