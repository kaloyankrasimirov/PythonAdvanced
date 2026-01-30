with open("text.txt") as f:
    for idx, line in enumerate(f):
        if idx % 2 == 0:
            for  ch in "-,.!?":
                line = line.replace(ch, "@")
            print(" ".join(reversed(line.split())))