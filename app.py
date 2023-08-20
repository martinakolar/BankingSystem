from bankingSystem import User, Bank
from bankingFunctions import catchOtherInfo
from userRegister import registration
from userLogin import verifyLogin


success = False
# * log in or register
while True:            
    print("\nWelcome to the Banking System")
    print("1. Register")
    print("2. Log in")

    user_choice = input("\nEnter your choice: ")

    if user_choice == "1":
        username, date_of_birth, home_address, initial_deposit_amount = registration()
        success = True
        break

    elif user_choice == "2":
        username = verifyLogin()
        if username is not False:
            success = True
            break
        else:
            success = False
            break
    else:
        print("Invalid choice")
        continue

if success is True:
    date_of_birth, home_address, initial_deposit_amount = catchOtherInfo(username)

    bank = Bank(username, date_of_birth, home_address, initial_deposit_amount)
    user = User(username, date_of_birth, home_address, initial_deposit_amount)


    while True:

        print("\n1. User details")
        print("2. Money transfer")
        print("3. View balance")
        print("4. View transaction history")
        print("5. Exit")

        bank_choice = input("\nEnter your choice: ")

        if bank_choice == "1":
            print(str(user))
        elif bank_choice == "2":
            bank.money_transfer()
        elif bank_choice == "3":
            bank.view_balance()
        elif bank_choice == "4":
            user.view_transaction_history()
        elif bank_choice == "5":
            print("Exiting...")
            exit()
        else:
            print("Invalid choice")

else:
    print("You do not have access to this database. Please try again later.")