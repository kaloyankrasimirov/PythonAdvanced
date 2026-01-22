from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milks = deque(int(x) for x in input().split(", "))

milkshakes = 0

while chocolates and milks and milkshakes < 5:
    if chocolates[-1] <= 0 and milks[0] <= 0:
        chocolates.pop()
        milks.popleft()
        continue
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if milks[0] <= 0:
        milks.popleft()
        continue

    if chocolates[-1] == milks[0]:
        milkshakes += 1
        chocolates.pop()
        milks.popleft()
    else:
        milks.rotate(-1)
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(el) for el in chocolates) if chocolates else 'empty'}")
print(f"Milk: {', '.join(str(el) for el in milks) if milks else 'empty'}")