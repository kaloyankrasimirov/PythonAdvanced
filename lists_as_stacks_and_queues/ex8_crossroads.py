from collections import deque

green_light_duration = int(input())
free_window = int(input())
total_cars_passed = 0
is_crash = False
car_queue = deque([])

while True:
    command = input()

    if command == "END":
        break

    if command == "green":
        current_green = green_light_duration
        while current_green > 0 and car_queue:
            current_car = car_queue.popleft()
            if len(current_car) <= current_green:
                current_green -= len(current_car)
                total_cars_passed += 1
            elif len(current_car) <= current_green + free_window:
                current_green = 0
                total_cars_passed += 1
            else:
                hit_box = current_green + free_window
                is_crash = True
                print("A crash happened!""\n"
                      f"{current_car} was hit at {current_car[hit_box]}.")
                break
    else:
        car_queue.append(command)

    if is_crash:
        break

if not is_crash:
    print("Everyone is safe.""\n"
          f"{total_cars_passed} total cars passed the crossroads.")

