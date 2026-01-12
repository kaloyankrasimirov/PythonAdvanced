initial_numbers = input().split()

stack = []
while initial_numbers:
    stack.append(initial_numbers.pop())

print(" ".join(stack))

