def registration():
    print("SIGN UP")

    #*registering the username
    min_username_and_password_len = 4
    while True:
        username = input("Username: ")

        if checkingIfUserAlreadyRegistered(username) == False:
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
            with open("userData.txt", "a") as file:
                file.write(username + "|" + password + "\n")
                print("Registration successful!")
                return True
            file.close()
        else:
            print("Passwords do not match!")


def checkingIfUserAlreadyRegistered(username):
        with open("userData.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split("|")
                if data[0] == username:
                    return False
            else:
                return True
            file.close()
                

registration()

