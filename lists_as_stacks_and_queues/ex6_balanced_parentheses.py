from collections import deque

sequence = input()
stack = deque([])
matches = {'{': '}', '[': ']', '(': ')'}
is_balanced = True

for symbol in sequence:
    if symbol in "{[(":
        stack.append(symbol)
    elif symbol in "}])":
        if not stack:
            is_balanced = False
            break
        elif symbol != matches[stack.pop()]:
            is_balanced = False
            break

if is_balanced and not stack:
    print("YES")
else:
    print("NO")
