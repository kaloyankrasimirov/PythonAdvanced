from collections import deque

robots_sequence = input().split(";")
robots = []

for _ in robots_sequence:
    name, proc_time = _.split("-")
    robots.append({
        'name': name,
        'proc_time': int(proc_time),
        'available_at': 0
    })

h, m, s = map(int, input().split(':'))
current_time_seconds = h * 3600 + m * 60 + s

products = deque()
while True:
    product_input = input()
    if product_input == "End":
        break
    products.append(product_input)

while products:
    current_time_seconds += 1
    current_product = products.popleft()

    found_robot = False
    for robot in robots:
        if robot['available_at'] <= current_time_seconds:
            robot['available_at'] = current_time_seconds + robot['proc_time']

            hrs = (current_time_seconds // 3600) % 24
            mins = (current_time_seconds // 60) % 60
            secs = current_time_seconds % 60

            print(f"{robot['name']} - {current_product} [{hrs:02d}:{mins:02d}:{secs:02d}]")
            found_robot = True
            break

    if not found_robot:
        products.append(current_product)