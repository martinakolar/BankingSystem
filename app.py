from bankingSystem import User, Bank, inputtingInitialDeposit
from userRegister import registration
from userLogin import verifyLogin, catchOtherInfo


def main():
    success = False
    # * log in or register
    while True:            
        print("\nWelcome to the Banking System")
        print("1. Register")
        print("2. Log in")

        user_choice = input("\nEnter your choice: ")

        if user_choice == "1":
            username, date_of_birth, home_address = registration()
            success = True
            break

        elif user_choice == "2":
            username = verifyLogin()
            if username != False:
                success = True
                break
            else:
                success = False
                break
        else:
            print("Invalid choice")
            continue

    if success is True:
        date_of_birth, home_address = catchOtherInfo(username)
        
        initial_deposit_amount = inputtingInitialDeposit()

        user = User(username, date_of_birth, home_address, initial_deposit_amount)
        bank = Bank(username, date_of_birth, home_address, initial_deposit_amount)


        while True:

            print("\n1. User details")
            print("2. Deposit money")
            print("3. Withdraw money")
            print("4. View balance")
            print("5. View transaction history")
            print("6. Exit")

            bank_choice = input("\nEnter your choice: ")

            if bank_choice == "1":
                info = user.user_details()
                print(info)
            elif bank_choice == "2":
                deposit_amount = float(input("Enter your deposit amount: "))
                bank.deposit_money(deposit_amount)
            elif bank_choice == "3":
                withdraw_amount = float(input("Enter your withdraw amount: "))
                bank.withdraw_money(withdraw_amount)
            elif bank_choice == "4":
                bank.view_balance()
            elif bank_choice == "5":
                bank.view_transaction_history()
            elif bank_choice == "6":
                print("Exiting...")
                exit()
            else:
                print("Invalid choice")

    else:
        print("You do not have access to this database. Please try again later.")


if __name__ == "__main__":
    main()