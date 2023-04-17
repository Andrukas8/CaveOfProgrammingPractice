people = ["Amelia", "Arthut", "Isla", "Noah", "Ava", "Leo", "Mia", "Oscar"]
ages = [20, 30, 25, 65, 21, 70, 32, 45]

people_ages_dict = dict()

for i in range(0,len(people)):
    people_ages_dict[people[i]] = ages[i]



do_loop = True

while do_loop:
    usr_input = input("Enter a name > ")
    if usr_input == "quit":
        do_loop = False
        break
    if usr_input in people_ages_dict:
        print(people_ages_dict[usr_input])
    else:
        print("Unknown person")