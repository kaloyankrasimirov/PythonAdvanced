from collections import deque
bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(y) for y in input().split()])
intelligence_value = int(input())

bullets_fired = 0

while bullets and locks:
    bullets_fired += 1
    current_bullet = bullets.pop()
    intelligence_value -= bullet_price
    if locks[0] >= current_bullet:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    if bullets_fired == gun_barrel_size and bullets:
        print("Reloading!")
        bullets_fired = 0

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value}")