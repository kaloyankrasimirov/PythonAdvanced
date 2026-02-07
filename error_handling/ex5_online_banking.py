class MoneyNotEnoughError(Exception):
    pass

class PINCodeError(Exception):
    pass

class UnderageTransactionError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass

pin, balance, age = [float(x) if i == 1 else int(x) for i, x in enumerate(input().split(", "))]


while True:
    command = input().split("#")

    if command[0] == "End":
        break

    action = command[0]

    if action == "Send Money":
        money = float(command[1])
        current_pin = int(command[2])

        if balance < int(money):
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        elif int(current_pin) != pin:
            raise PINCodeError("Invalid PIN code")
        elif age < 18:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        balance -= float(command[1])
        print(f"Successfully sent {money:.2f} to a friend""\n"
              f'There is {balance:.2f} money left in the account')



    if action == "Receive Money":
        money = float(command[1])
        if int(money) < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        balance += float(command[1]) / 2

        print(f"{(money / 2):.2f} money went straight into the bank account")





