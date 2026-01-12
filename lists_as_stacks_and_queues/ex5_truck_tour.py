from collections import deque

pumps_num = int(input())
pumps = deque()

for _ in range(pumps_num):
    current_fuel, current_distance = input().split()
    pumps.append({"fuel": int(current_fuel), "dist": int(current_distance)})

start_point = 0
stops = 0

while stops < pumps_num:
    fuel = 0
    for i in range(pumps_num):
        fuel += pumps[i]["fuel"]
        distance = pumps[i]["dist"]
        if fuel < distance:
            pumps.rotate(-1)
            start_point += 1
            stops = 0
            break
        fuel -= distance
        stops += 1

print(start_point)