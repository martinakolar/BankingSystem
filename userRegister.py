import bcrypt
from bankingFunctions import checkingIfUserAlreadyRegistered, getDateOfBirth, inputtingInitialDeposit 


def registration():
    print("SIGN UP")

    #*registering the username
    min_username_and_password_len = 4
    while True:
        username = input("Username: ")

        if checkingIfUserAlreadyRegistered(username):
            print("This user has already been registered.")
            continue

        if len(username) < min_username_and_password_len:
            print("Username must be at least 4 characters long!")
            continue
        
        else:
            break

    #*registering the password
    while True:

        password = input("Password: ")
        while len(password) < min_username_and_password_len:
            print("Password must be at least 4 characters long!")
            password = input("Password: ")

        confirm_password = input("Confirm password: ")
        if confirm_password == password:
            hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
            print("Password stored.")
            break
        else:
            print("Passwords do not match!")
            continue

    #*date of birth
    date_of_birth = getDateOfBirth(username)

    #*home address
    home_address = input("Home address: ")

    #*initial deposit
    initial_deposit = inputtingInitialDeposit()

    with open("userData.txt", "a") as file:
        file.write(username + "|" + hashed_password.decode('utf-8') + "|" + home_address + "|" + date_of_birth + "|" + str(initial_deposit) + "\n")
        print("Registration successful!")
    file.close()

    return username, date_of_birth, home_address, initial_deposit