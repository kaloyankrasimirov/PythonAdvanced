seq_storage = []


def create_fibonacci(n):
    seq = [0, 1]
    for num in range(n-2):
        seq.append(seq[-1] + seq[-2])
    return seq

def locate(num, sequence):
    try:
        return sequence.index(num)
    except ValueError:
        return None

def dispatcher(some_command):
    global seq_storage

    if some_command.startswith("Create"):
        num = int(some_command.split()[-1])
        seq_storage = create_fibonacci(num)
        return " ".join(map(str, seq_storage))
    elif some_command.startswith("Locate"):

        num = int(some_command.split()[-1])
        index = locate(num, seq_storage)

        if isinstance(index, int):
            return f"The number - {num} is at index {index}"
        else:
            return f"The number {num} is not in the sequence"
    return ""




