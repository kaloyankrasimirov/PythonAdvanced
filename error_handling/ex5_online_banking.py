class MoneyNotEnoughError(Exception):
    pass

class PINCodeError(Exception):
    pass

class UnderageTransactionError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass

pin, balance, age = [int(x) for x in input().split(", ")]


while True:
    command = input()

    if command == "End":
        break

    parts = command.split("#")

    action = parts[0]

    if action == "Send Money":
        money = int(parts[1])
        current_pin = int(parts[2])

        if balance < int(money):
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        elif int(current_pin) != pin:
            raise PINCodeError("Invalid PIN code")
        elif age < 18:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        balance -= int(parts[1])
        print(f"Successfully sent {money:.2f} to a friend""\n"
              f'There is {balance - money:.2f} money left in the account')



    if action == "Receive Money":
        money = int(parts[1])
        if int(money) < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        balance += int(parts[1]) / 2

        print(f"{(money / 2):.2f} money went straight into the bank account")





