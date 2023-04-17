
def create_lookup(people, ages):
    lookup = dict()
    for name, age in zip(people, ages):
        lookup[name.casefold()] = age
    return lookup

def user_loop(lookup):
    while True:
        user_input = input("Enter a name or 'quit' > ")

        if user_input == "quit":
            break
       
        age = lookup.get(user_input.casefold())

        if age is None:           
            continue

        print(user_input + " is " + str(age) + " years old")

def main():
    people = ["Amelia", "Arthur", "Isla", "Noah", "Ava", "Leo", "Mia", "Oscar"]
    ages = [20, 30, 25, 65, 21, 70, 32, 45]

    lookup = create_lookup(people, ages)

    user_loop(lookup)

main()

