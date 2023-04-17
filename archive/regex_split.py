import re
def main():
    text = "one,two,three,four"
    fields = re.split(r",*,\s*", text)

    print(fields)

main()

