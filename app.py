from bankingSystem import User, Bank
from userRegister import registration
from userLogin import verifyLogin


def main():
    # * log in or register
    while True:            
        print("Welcome to the Banking System")
        print("1. Register")
        print("2. Log in")

        user_choice = int(input("Enter your choice: "))
        if user_choice == 1:
            registration()
            break
        elif user_choice == 2:
            verifyLogin()
            break
        else:
            print("Invalid choice")

    bank = Bank("username", "address", "25.08.2001.")

    """
    while True:

        print("1. User details")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. View balance")
        print("5. Exit")

        bank_choice = int(input("Enter your choice: "))

        if bank_choice == 1:
            bank.user_details()
        elif bank_choice == 2:
            deposit_amount = float(input("Enter your deposit amount: "))
            bank.deposit(deposit_amount)
        elif bank_choice == 3:
            withdraw_amount = float(input("Enter your withdraw amount: "))
            bank.withdraw(withdraw_amount)
        elif bank_choice == 4:
            bank.viewbalance()
        elif bank_choice == 5:
            print("Exiting...")
            exit()
        else:
            print("Invalid choice")"""


if __name__ == "__main__":
    main()