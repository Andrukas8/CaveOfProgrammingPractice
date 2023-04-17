def main():
    fruits = {
        "apple": "green",
        "orange": "orange",
        "banana": "yellow",
    }

    del fruits["apple"]

    fruits.pop("banana")

    for fruit in fruits:
        print(fruit + ": " + fruits[fruit])


main()

