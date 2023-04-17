def test(name, *args, **kwargs):
    print(name)
    for arg in args:
        print(arg)

    for key in kwargs:
        print(key," = ",kwargs[key])


def main():
    test("Bob", 0, 1, 2, color="green", value=8)

main()