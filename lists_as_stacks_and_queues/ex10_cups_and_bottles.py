from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]
wasted_water = 0

while cups and bottles:
    while len(cups) > 0:
        current_bottle = bottles.pop()

        cups[0] -= current_bottle
        if cups[0] <= 0:
            wasted_water += abs(cups[0])
            cups.popleft()
            break

if not cups:
    print(f"Bottles: {' '.join(map(str, bottles))}")
if not bottles:
    print(f"Cups: {' '.join(map(str, cups))}")
print(f"Wasted litters of water: {wasted_water}")