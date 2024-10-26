class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

    def __str__(self):
        status = "Borrowed" if self.borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.borrowed:
                book.borrowed = True
                print(f"You have borrowed '{title}'.")
                return
        print("Book not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.borrowed:
                book.borrowed = False
                print(f"You have returned '{title}'.")
                return
        print("Book not found or not borrowed.")

    def list_books(self):
        for book in self.books:
            print(book)

def main():
    library = Library()
    while True:
        print("\n1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. List Books")
        print("5. Quit")

        choice = input("Enter your choice: ")
        if choice == '5':
            break
        elif choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == '2':
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)
        elif choice == '3':
            title = input("Enter book title to return: ")
            library.return_book(title)
        elif choice == '4':
            library.list_books()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
