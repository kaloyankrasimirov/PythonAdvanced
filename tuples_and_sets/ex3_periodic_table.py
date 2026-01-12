# print(*{el for _ in range(int(input())) for el in input().split()}, sep="\n")

elements = set()

# for _ in range(int(input())):
#     for el in input().split():
#         elements.add(el)
#
# print(*elements, sep="\n")

for el in range(int(input())):
    elements = elements.union(input().split())

print(*elements, sep="\n")