string = input()
stack = []

for i in range(len(string)):
    if string[i] == "(":
        stack.append(i)
    elif string[i] == ")":
        start_index = stack.pop()
        end_index = i + 1
        print(string[start_index:end_index])
