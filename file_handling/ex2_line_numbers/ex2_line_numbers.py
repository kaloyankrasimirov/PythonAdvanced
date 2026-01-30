from string import punctuation

with open("text.txt") as input_file, open("output.txt", "w") as output_file:
    result = []
    for row, line in enumerate(input_file):
        letter_count = 0
        punctuation_count = 0

        for symbol in line:
            if symbol.isalpha():
                letter_count += 1
            elif symbol in punctuation:
                punctuation_count += 1

        result.append(f"Line {row+1}: {line.strip()} ({letter_count})({punctuation_count})")

    output_file.write("\n".join(result))