from math import log

num = int(input())
try:
    base = int(input())
    print(f"{log(num, base):.2f}")
except ValueError:
    print(f"{log(num):.2f}")