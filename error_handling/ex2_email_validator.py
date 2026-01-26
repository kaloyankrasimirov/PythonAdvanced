class NameTooShortError(Exception):
    pass

class MustContainASymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

EMAIL_MIN_LEN = 5
VALID_DOMAINS = ["com", "bg", "net", "org"]

while True:
    line = input()
    if line == "End":
        break

    if "@" not in line:
        raise MustContainASymbolError("Email must contain @")

    if len(line.split("@")[0]) < EMAIL_MIN_LEN:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = line.split(".")[-1]

    if domain not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")


    print("Email is valid")
