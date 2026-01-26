text = input()

while True:
    try:
        times = int(input())
        print((text+" ") *times)
        break
    except ValueError as err:
        print(f"Variable times must be an integer."'\n'
              f"Original Trace: {err}")