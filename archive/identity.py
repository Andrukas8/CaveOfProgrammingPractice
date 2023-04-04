def greet(name):
    print("Hello " + name)
    print(id(name))

def main():
    name = "John"
    print(id(name))
    greet(name)

main()


