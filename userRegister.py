def registration():
    print("SIGN UP")
    min_username_len = 4

    username = input("Username: ")
    while len(username) < min_username_len or checkingIfUserAlreadyRegistered(username) == False:
        if len(username) < min_username_len:
            print("Username must be at least 4 characters long!")
        username = input("Username: ")

    while True:
        password = input("Password: ")
        while len(password) < 3:
            print("Password is too short!")
            password = input("Password: ")
        confirm_password = input("Confirm password: ")

        if confirm_password == password:
            with open("userData.txt", "a") as file:
                file.write(username + "|" + password + "\n")
                file.close()
                print("Registration successful!")
                break
        else:
            print("Passwords do not match!")
            continue

def checkingIfUserAlreadyRegistered(username):
        with open("userData.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split("|")
                if data[0] == username:
                    print("This user has already been registered.")
                    return False
                else:
                    return True
            file.close()
                

registration()

