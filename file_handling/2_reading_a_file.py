import os
from constants import path_to_dir

path = os.path.join(path_to_dir, "files", "numbers.txt")

file = open(path)

# numbers = [int(x) for x in file.read().split("\n") if x]

total = 0
for line in file:
    total += int(line)
print(total)