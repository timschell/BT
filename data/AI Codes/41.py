class Book:
    def __init__(self, title, author, review=None):
        self.title = title
        self.author = author
        self.review = review

    def __str__(self):
        return f"{self.title} by {self.author} - Review: {self.review if self.review else 'No review yet'}"

class BookReviewTracker:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def add_review(self, title, review):
        for book in self.books:
            if book.title == title:
                book.review = review
                return
        print("Book not found.")

    def list_books(self):
        for book in self.books:
            print(book)

def main():
    tracker = BookReviewTracker()
    while True:
        print("\n1. Add Book")
        print("2. Add Review")
        print("3. List Books")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '4':
            break
        elif choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            tracker.add_book(title, author)
        elif choice == '2':
            title = input("Enter book title to review: ")
            review = input("Enter your review: ")
            tracker.add_review(title, review)
        elif choice == '3':
            tracker.list_books()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
