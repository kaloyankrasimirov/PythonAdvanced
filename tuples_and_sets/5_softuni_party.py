n = int(input())
reservations = set()

for _ in range(n):
    reservation = input()
    reservations.add(reservation)

reservation = input()

while reservation != "END":
    reservations.discard(reservation)
    reservation = input()

print(len(reservations))
sorted_reservations = sorted(reservations)

for reservation in sorted_reservations:
    print(reservation)