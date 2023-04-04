def main():
    elements = (True, 3.2, 7, "goat")

    (is_raining, weight, volume, animal) = elements

    print(is_raining, weight, volume, animal)

    fruits = ("apple", "orange", "banana", "strawberry", "pear")

    (fruit1, fruit2, fruit3, *more_fruits) = fruits

    print(fruit1, fruit2, fruit3, more_fruits)

    print(type(more_fruits))

    fruits = ("apple", "orange", "banana", "strawberry", "pear")

    (fruit1, fruit2,  *more_fruits, fruit3) = fruits
    print(more_fruits)



main()