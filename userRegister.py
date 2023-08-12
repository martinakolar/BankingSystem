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
            print("Password stored.")
            break
        else:
            print("Passwords do not match!")
            continue

    #*date of birth
    print("Date of birth: ")

    day_of_birth = int(input("Day(DD): "))
    while day_of_birth < 1 or day_of_birth > 31:
        print("Day of birth must be between 1 and 31!")
        day_of_birth = int(input("Day(DD): "))

    month_of_birth = int(input("Month(MM): "))
    while month_of_birth < 1 or month_of_birth > 12:
        print("Month of birth must be between 1 and 12!")
        month_of_birth = int(input("Month(MM): "))

    year_of_birth = int(input("Year(YYYY): "))
    while year_of_birth < 1900 or year_of_birth > 2023:
        print("Year of birth must be between 1900 and 2023!")
        year_of_birth = int(input("Year(YYYY): "))


    date_of_birth = f"{day_of_birth}.{month_of_birth}.{year_of_birth}"

    #*home address
    home_address = input("Home address: ")

    with open("userData.txt", "a") as file:
        file.write(username + "|" + password + "|" + home_address + "|" + date_of_birth + "\n")
        print("Registration successful!")
    file.close()

    return username, date_of_birth, home_address




def checkingIfUserAlreadyRegistered(username):
        with open("userData.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split("|")
                if data[0] == username:
                    return False
            else:
                return True


registration()
