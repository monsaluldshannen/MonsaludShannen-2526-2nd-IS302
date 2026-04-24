def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open("users.txt", "a") as file:
        file.write(username + "," + password + "\n")
    print("User registered successfully!\n")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    found = False
    try:
        with open("users.txt", "r") as file:
            for line in file:
                stored_user, stored_pass = line.strip().split(",")
                if username == stored_user and password == stored_pass:
                    found = True
                    break
        if found:
            print("Login successful!\n")
        else:
            print("Invalid username or password.\n")
    except FileNotFoundError:
        print("No registered users found. Please register first.\n")

while True:
    print("Menu:\n1 Register\n2 Login\n3 Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.\n")