from models import Author, Book, session

def display_menu():
    print("\nLibrary Management System")
    print("1. List all authors")
    print("2. List all books")
    print("3. Add an author")
    print("4. Add a book")
    print("5. Delete an author")
    print("6. Delete a book")
    print("7. Find author by ID")
    print("8. Find book by ID")
    print("9. Exit")

def list_authors():
    authors = Author.get_all()
    for author in authors:
        print(author)

def list_books():
    books = Book.get_all()
    for book in books:
        print(book)

def add_author():
    name = input("Enter author name: ")
    Author.create(name)
    print("Author added successfully!")

def add_book():
    title = input("Enter book title: ")
    author_id = input("Enter author ID: ")
    Book.create(title, author_id)
    print("Book added successfully!")

def delete_author():
    author_id = input("Enter author ID to delete: ")
    if Author.delete(author_id):
        print("Author deleted successfully!")
    else:
        print("Author not found.")

def delete_book():
    book_id = input("Enter book ID to delete: ")
    if Book.delete(book_id):
        print("Book deleted successfully!")
    else:
        print("Book not found.")

def find_author_by_id():
    author_id = input("Enter author ID: ")
    author = Author.find_by_id(author_id)
    if author:
        print(author)
    else:
        print("Author not found.")

def find_book_by_id():
    book_id = input("Enter book ID: ")
    book = Book.find_by_id(book_id)
    if book:
        print(book)
    else:
        print("Book not found.")

def main():
    while True:
        display_menu()
        choice = input("> ")
        if choice == "1":
            list_authors()
        elif choice == "2":
            list_books()
        elif choice == "3":
            add_author()
        elif choice == "4":
            add_book()
        elif choice == "5":
            delete_author()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            find_author_by_id()
        elif choice == "8":
            find_book_by_id()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

