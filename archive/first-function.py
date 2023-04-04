response = input("How are you? : ")


def ask_user_status():
    if response == "OK" or response == "ok":
        print("Excellent!")
    else:
        print("Oh no.")

ask_user_status()