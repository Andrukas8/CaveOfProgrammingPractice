import re

def main():
    text = "Hello Jack"

    text = re.sub("J\w+", "Zoe", text)

    print(text)

main()