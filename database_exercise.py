def show_menu():
    options = ("Display the DB", "Add Item", "Delete Item", "Change Item", "Quit")
    print()
    for i in range(0, len(options)):
        print(str(i + 1) + ": " + options[i])
    print()

def show_database(db):
    print()
    for i in range(0, len(db)):
        print(str(i) + ": " + db[i])
    print()

def add_item(db):
    item = input("Enter item to add: ")
    db.append(item)

def change_item(db):
    item_number = input("Enter number of item to change: ")
    item = input("Enter new item: ")
    db[int(item_number)] = item

def delete_item(db):
    item_number = input("Enter number of item to delete: ")
    db.pop(int(item_number))



def main():
    db = ["apple", "orange", "mango"]

    do_loop = True

    while do_loop:
        show_menu()
        option = input("Select Option > ")

        if option == "1":
            show_database(db)
        elif option == "2":
            add_item(db)
        elif option == "3":
            delete_item(db)
        elif option == "4":
            change_item(db)
        elif option == "5":
            do_loop = False
        else:
            print("Unrecognized option...")


main()