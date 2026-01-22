raw_matrix = [x for x in input().split("|")]
final_list = []

for i in range(len(raw_matrix) -1, -1, -1):
    data = raw_matrix[i].split()
    final_list.extend(data)

print(*final_list)