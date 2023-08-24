from datetime import datetime


#*for the login function
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




#*for the banking function
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




#*for the registration function
def checkingIfUserAlreadyRegistered(username):
        with open("userData.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split("|")
                if data[0] == username:
                    return True
            else:
                return False



def getDateOfBirth(username):
    print("Date of birth: ")

    day_of_birth = int(input("Day(DD): "))
    while day_of_birth < 1 or day_of_birth > 31:
        print("Day of birth must be between 1 and 31!")
        day_of_birth = int(input("Day(DD): "))

    month_of_birth = int(input("Month(MM): "))
    while month_of_birth < 1 or month_of_birth > 12:
        print("Month of birth must be between 1 and 12!")
        month_of_birth = int(input("Month(MM): "))

    year_of_birth = int(input("Year(YYYY): "))
    while year_of_birth < 1900 or year_of_birth > 2023:
        print("Year of birth must be between 1900 and 2023!")
        year_of_birth = int(input("Year(YYYY): "))


    date_of_birth = f"{day_of_birth}.{month_of_birth}.{year_of_birth}"
    return date_of_birth



def inputtingInitialDeposit():
    initial_deposit_bool = input("\nDo you wish to make an initial deposit? (y/n): ").lower() 
    if initial_deposit_bool == "y":
        while True:
            try:
                initial_deposit_amount = float(input("Enter your initial deposit amount: "))
            except ValueError:
                print("Please enter a valid initial deposit amount.")
                continue
            else:
                print("Initial deposit amount successfully made.")
                return initial_deposit_amount
    else:
        initial_deposit_amount = 0
        return initial_deposit_amount