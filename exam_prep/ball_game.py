from collections import deque

strength_values = [int(x) for x in input().split()]
accuracy_values = deque(int(x) for x in input().split())
goals = 0

while strength_values and accuracy_values:
    current_str = strength_values[-1]
    current_accu = accuracy_values[0]

    if current_accu + current_str == 100:
        goals += 1
        strength_values.pop()
        accuracy_values.popleft()
    elif current_accu + current_str < 100:
        if current_str < current_accu:
            strength_values.pop()
        elif current_str > current_accu:
            accuracy_values.popleft()
        else:
            strength_values[-1] = current_str + current_accu
            accuracy_values.popleft()
    else:
        strength_values[-1] = current_str - 10
        accuracy_values.append(accuracy_values.popleft())

if goals == 3:
    print("Paul scored a hat-trick!")
elif goals <= 0:
    print("Paul failed to score a single goal.")
elif goals > 3:
    print("Paul performed remarkably well!")
elif 0 < goals < 3:
    print("Paul failed to make a hat-trick.")
if goals > 0:
    print(f"Goals scored: {goals}")

if strength_values:
    print(f"Strength values left: {', '.join(map(str, strength_values))}")
elif accuracy_values:
    print(f"Accuracy values left: {', '.join(map(str, accuracy_values))}")
