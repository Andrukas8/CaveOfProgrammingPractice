def main():
    cubic_set = {x**3 for x in range(10)}    
    print(cubic_set)

    square_set = {x**2 for x in range(28)}
    print(square_set)

    print()

    print(cubic_set.intersection(square_set))
    print(cubic_set - square_set)

main()