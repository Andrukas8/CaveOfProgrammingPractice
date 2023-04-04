def main():
    fruits = {
        "apple": "green",
        "orange": "orange",
        "banana": "yellow",
    }


    color = fruits.get("mango", "red")

    print(color)

main()