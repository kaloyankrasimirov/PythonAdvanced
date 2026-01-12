n = int(input())
parking_lot = set()

for _ in range(n):
    direction, reg = input().split(", ")
    if direction == "IN":
        parking_lot.add(reg)
    else:
        parking_lot.discard(reg)

if not parking_lot:
    print("Parking Lot is Empty")
else:
    for reg in parking_lot:
        print(reg)