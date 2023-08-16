def verifyLogin():
    print("LOG IN")
    username = input("Username: ")
    password = input("Password: ")

    attempts = 1
    logged_in = False

    with open("userData.txt", "r") as file:
        lines = file.readlines()

        for line in lines:

            data = line.strip().split("|")

            if data[0] == username and data[1] == password:
                print("Login successful!")
                logged_in = True
                return username
            elif data[0] != username:
                print("This username doesn't exist.")
                return False
            elif data[0] == username and data[1] != password:

                while True:
                    print(f"Login failed. {attempts}")
                    username = input("Username: ")
                    password = input("Password: ")

                    if username == data[0] and password == data[1]:
                        print("Login successful!")
                        logged_in = True
                        return username
                    else:
                        attempts += 1
                        if attempts == 3:
                            print("Login failed. Account has been temporarily blocked for security reasons.")
                            return False
                        else:
                            continue

        if not logged_in:
            print("Login failed.")
            return False
        file.close()



def catchOtherInfo(username):
    with open("userData.txt", "r") as file:
        lines = file.readlines()

        for line in lines:

            data = line.strip().split("|")

            if data[0] == username:
                date_of_birth = data[2]
                home_address = data[3]
                initial_deposit = data[4]
        file.close()

    return date_of_birth, home_address, initial_deposit

