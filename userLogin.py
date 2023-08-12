def verifyLogin():
    print("LOG IN")
    username = input("Username: ")
    password = input("Password: ")

    logged_in = False

    with open("userData.txt", "r") as file:
        lines = file.readlines()

        for line in lines:

            data = line.strip().split("|")

            if data[0] == username and data[1] == password:
                print("Login successful!")
                logged_in = True
                date_of_birth, home_address = catchOtherInfo(username)

        if not logged_in:
            print("Login failed.")
        file.close()

        return username, date_of_birth, home_address


def catchOtherInfo(username):
    with open("userData.txt", "r") as file:
        lines = file.readlines()

        for line in lines:

            data = line.strip().split("|")

            if data[0] == username:
                date_of_birth = data[2]
                home_address = data[3]
        file.close()

    return date_of_birth, home_address


