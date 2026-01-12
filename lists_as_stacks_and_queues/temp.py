from collections import deque

queue = deque(["Ivan", "Parvan", "Dragan"])
queue.append("Stamat")
print(queue)

queue.popleft()
print(queue)