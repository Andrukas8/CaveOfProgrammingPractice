def main():
    numbers1 = {1, 2, 3, 4, 5, 6, 7}
    numbers2 = {8, 0, 3, 10, 5, 6, 7}

    # print(numbers1.union(numbers2))

    # print(numbers1.intersection(numbers2))

    # print(numbers1.difference(numbers2))

    # print(numbers2.symmetric_difference(numbers1))

    # print(numbers1 - numbers2)

    numbers1.difference_update(numbers2)
    print(numbers1)


main()