def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)


def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print(f"Book {book_id} borrowed successfully.")
    else:
        print(f"Book {book_id} cannot be borrowed (not found or already borrowed).")


def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book {book_id} returned successfully.")
    else:
        print(f"Book {book_id} was not borrowed.")


def register_member(members, member_id):
    if member_id in members:
        print(f"Member {member_id} already registered. Ignored.")
    else:
        members.add(member_id)
        print(f"Member {member_id} registered.")


def show_available(catalog, borrowed_books):
    print("Available Books:")
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"  {book_id}: {title} by {author} ({year})")


def main():
    catalog = {}
    borrowed_books = []
    members = set()

    add_book(catalog, 1, "Python Basics", "A. Sharma", 2020)
    add_book(catalog, 2, "Data Structures", "R. Gupta", 2019)
    add_book(catalog, 3, "Algorithms 101", "S. Rao", 2021)
    add_book(catalog, 4, "Clean Code", "R. Martin", 2008)

    register_member(members, 101)
    register_member(members, 102)
    register_member(members, 103)
    register_member(members, 101)

    borrow_book(catalog, borrowed_books, 1)
    borrow_book(catalog, borrowed_books, 2)

    return_book(borrowed_books, 1)

    show_available(catalog, borrowed_books)
    print("Registered members:", members)


if __name__ == "__main__":
    main()