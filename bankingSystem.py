from bankingFunctions import typeOfMoneyTransfer, appendingToTransactionHistory



class Bank():
    transaction_history = {}
    
    def __init__(self, full_name, address, date_of_birth, initial_deposit_amount=None):
        self.full_name = full_name
        self.address = address
        self.date_of_birth = date_of_birth
        if initial_deposit_amount is not None:
            self.initial_deposit_amount = initial_deposit_amount
        else:
            self.initial_deposit_amount = 0
        #!this will need to be fixed in the future
        self.balance = float(initial_deposit_amount)
        

    def money_transfer(self):

        type = typeOfMoneyTransfer()

        try:
            amount = float(input("Enter the amount to transfer: "))

        #*invalid input
        except ValueError:
            print("Sorry, your input is invalid. Try again.")

        #*correct input
        else:
            
            if type == "deposit":
                if amount > 0:
                    self.balance += amount
                    appendingToTransactionHistory(self.transaction_history, type, amount)
                    
                    print(f"Account balance has been increased by €{amount}.")

                else:
                    print("You cannot deposit a negative amount.")

            elif type == "withdrawal":
                if amount > 0:
                    if amount <= self.balance:
                        self.balance -= amount
                        appendingToTransactionHistory(self.transaction_history, type, amount)

                        print(f"You have successfully withdrawn €{amount}.")
                    else:
                        print("Your current balance is lower than the amount you want to withdraw.")

                else:
                    print("You cannot withdraw a negative amount.")
        

    def view_balance(self):
        print(f"Your current account balance is €{self.balance}.")





class User(Bank):
    
    def __init__(self, full_name, address, date_of_birth, initial_deposit_amount):
        super().__init__(full_name, address, date_of_birth, initial_deposit_amount)


    def __str__(self):
        return f"USER DETAILS \nName: {self.full_name} \nAddress: {self.address} \nDate of birth: {self.date_of_birth} \nInitial deposit amount: €{self.initial_deposit_amount}\n"


    def view_transaction_history(self):
        for key in self.transaction_history:
            print(key, '->', self.transaction_history[key])