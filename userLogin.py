import bcrypt

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

            #*username exists
            if data[0] == username:

                #*logged in at first attempt
                if bcrypt.checkpw(password.encode('utf-8'), data[1].encode('utf-8')) is True:
                    print("Login successful!")
                    logged_in = True
                    return username
                
                elif bcrypt.checkpw(password.encode('utf-8'), data[1].encode('utf-8')) is not True:
                    while True:
                        print(f"Login failed. {attempts}")
                        password = input("Password: ")

                        if bcrypt.checkpw(password.encode('utf-8'), data[1].encode('utf-8')) is True:
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