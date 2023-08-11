class User():
    
    def __init__(self, full_name, address, date_of_birth, initial_deposit_amount=0):
        self.full_name = full_name
        self.address = address
        self.date_of_birth = date_of_birth
        self.initial_deposit_amount = initial_deposit_amount

    def user_details(self):
        return f"USER DETAILS \nName: {self.full_name} \nAddress: {self.address} \nDate of birth: {self.date_of_birth} \nInitial deposit amount: €{self.initial_deposit_amount}\n"

class Bank(User):
    
    def __init__(self, full_name, address, date_of_birth, initial_deposit_amount=0):
        super().__init__(full_name, address, date_of_birth, initial_deposit_amount=0)
        self.balance = initial_deposit_amount
        
        
    def deposit_money(self, amount):
        self.amount = amount
        self.balance += self.amount
        print(f"Account balance has been increased by €{self.amount}.")
        
        
    def view_balance(self):
        print(f"Your current account balance is €{self.balance}.")
        
        
    def withdraw_money(self, amount):
        self.amount = amount
        
        if self.amount <= self.balance:
            self.balance -= self.amount
            print(f"You have successfully withdrawn €{self.amount}.")
        else:
            print("Your current balance is lower than the amount you want to withdraw.")
        

