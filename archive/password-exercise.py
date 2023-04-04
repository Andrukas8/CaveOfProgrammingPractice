PASSWORD = "hello"
for _ in range(3):
    password = input("Enter your password: ")
    if password == PASSWORD:
        print("Greetings Professor Falcon")
        break
    else:
        print("Access denied.")
