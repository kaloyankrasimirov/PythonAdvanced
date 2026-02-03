from modules.fibonacci_sequence.core import dispatcher

command = input()

while command != "Stop":
    result = dispatcher(command)
    if result:
        print(result)

    command = input()
