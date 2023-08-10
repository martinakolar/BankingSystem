def verifyLogin():
    print("SIGN IN")
    username = input("Username: ")
    password = input("Password: ")

    with open("userData.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split("|")
            if data[0] == username and data[1] == password:
                print("Login successful!")
                return True
            else:
                print("Login failed.")
                return False
        file.close()


verifyLogin()

