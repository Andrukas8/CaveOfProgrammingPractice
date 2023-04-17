value = 0
value = 1

def do_something():
    global value
    print(value)
    value = 10
    print(value)
    

def main():
    do_something()

main()