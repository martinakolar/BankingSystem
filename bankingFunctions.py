from datetime import datetime

def catchOtherInfo(username):
    with open("userData.txt", "r") as file:
        lines = file.readlines()

        for line in lines:

            data = line.strip().split("|")

            if data[0] == username:
                date_of_birth = data[2]
                home_address = data[3]
                initial_deposit = data[4]
        file.close()

    return date_of_birth, home_address, initial_deposit


def typeOfMoneyTransfer():
    while True:
        type = input("Would you like to deposit (1) or withdraw (2)? ")
        if type == "1":
            type = "deposit"
            return type
        elif type == "2":
            type = "withdrawal"	
            return type
        else:
            print("Please enter either 1 or 2.")
            continue


def appendingToTransactionHistory(transaction_history, type, amount):
    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M
    date_and_time = now.strftime("%d.%m.%Y. %H:%M:%S")

    # appending an item to the transaction history
    transaction_history[date_and_time] = f"{type}, €{amount}"