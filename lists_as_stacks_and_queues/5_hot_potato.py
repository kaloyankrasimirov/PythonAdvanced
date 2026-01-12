from collections import deque

kids = deque(input().split())
number = int(input())

while len(kids) > 1:
    kids.rotate(-number + 1) #-(n-1)
    print(f"Removed {kids.popleft()}")

print(f"Last is {kids.popleft()}")