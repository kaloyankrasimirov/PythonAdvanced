class CustomError(Exception):
    """"Base class for custom errors"""
    pass

class ValueCannotBeNegative(CustomError):
    """Raised when value is below 0"""

for n in range(5):
    n = int(input())
    if n < 0:
        raise ValueCannotBeNegative("Number cannot be negative")

