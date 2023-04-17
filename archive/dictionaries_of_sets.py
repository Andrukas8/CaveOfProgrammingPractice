def add_book(library, category, title):

    if not category in library:
        library[category] = set()
    library[category].add(title)


def print_library(library):
    for category in library:
        books = library[category]
        print(category + ": ", end="")

        print(", ".join(books))


def find_book(library, book):
    for books in library.values():
        if book in books:
            return True
    return False


def main():

    library = {
        "Science Fiction": {"Journey to the Center of the Earch", "Day of the Triffids"},
        "Drama": {"A Tale of Two Cities", "Moby Dick"},
    }

    add_book(library, "Science Fiction", "The War of the Worlds")

    print_library(library)

    print(find_book(library, "Moby Dick"))
    print(find_book(library, "Kuku"))



main()
