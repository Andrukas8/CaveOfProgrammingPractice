def main():
    name = "Zoe"
    text = "Hello %s. How are you?" % name

    print(text)
    print("Hello %s and %s. How are you today?" % ("Zoe", "Jack"))
    print("Hello %s, the temperature is %.2f How are you today?" % ("Zoe", 31.1234))
    print("Hello %s, the temperature is %10d How are you today?" % ("Zoe", 31))
    print("Hello %s, the temperature is %10.2f How are you today?" % ("Zoe", 31.1234))



main()