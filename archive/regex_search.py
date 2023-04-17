import re

def main():
    text = """
    one
    two
    three
    """

    result = re.search(r"t.*e", text, re.DOTALL)

    if result is None:
        print("No match")
    else:
        print(f"{result.group(0)}")

main()

