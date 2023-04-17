import re

def main():
    text = """
        one
        two
        three
    """

    print(re.match(r".*one", text, re.DOTALL))

main()