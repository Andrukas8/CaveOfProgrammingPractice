import re

def main():
    text = "Oranges are nice"

    regex = re.compile(r"O\w+s", flags = re.I)
    print(re.sub(regex, "Bananas", text))

main()