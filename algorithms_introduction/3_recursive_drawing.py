def print_figure(num):
    if num <= 0:
        return

    print("*" * num)

    print_figure(num -1)

    print("#" * num)


n = int(input())
print_figure(n)