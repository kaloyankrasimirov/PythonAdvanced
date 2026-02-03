signs = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "^": lambda x, y: x ** y
}

def calculator(some_string):
    num1, sign, num2 = some_string.split()
    return signs[sign](float(num1), float(num2))

