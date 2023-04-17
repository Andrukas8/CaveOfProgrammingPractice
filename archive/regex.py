import re

def main():
    text = "dog"

    result = re.match("d.g", text)    
    print(result is not None)


    text1 = "drooooool"
    result1 = re.match("dr.*l", text1)

    if result1 is None:
        print("No match")
    else:
        print(result1.group())

main()