
def calculate_bmi():
    weight = input("Enter your weight in kilos: ")
    height = input("enter your height in meters: ")

    weight = float(weight)
    height = float(height)

    bmi = weight / (height * height)

    return weight, height, bmi


def main():
    weight, height, bmi = calculate_bmi()
    print("weight =", weight, "height = ", height, "BMI =", bmi)

main()