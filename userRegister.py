def registration():

    username = input("Username: ")
    while len(username) <= 3:
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

registration()
