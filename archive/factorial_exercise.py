
def get_input():
    number = int(input("Please enter the number : "))
    return number

def calculate_factorial(number):    
    result = 1
    for i in range(2,number + 1):
        result = result * i
    return result


def main():
    number = get_input()
    result = calculate_factorial(number)
    print("Factorial of",number,"is",result)

main()