def main():
    numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 4, "A", "B", "C"]]

    sublist = numbers[1]
    print(sublist[2])
    print(numbers[2][1])

    for i in range(0, len(numbers)):
        for j in range(0,len(numbers[i])):
            print(numbers[i][j])

    for x in numbers:
        for y in x:
            print(y,end=" ")
        print()
    
    print()

    for i in range(0,len(numbers)):
        for j in range(0,len(numbers[i])):
            print(numbers[i][j], end=" ")
        print()
    
    print()

    



main()