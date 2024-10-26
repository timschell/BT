class Flashcard:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

    def __str__(self):
        return f"Term: {self.term}\nDefinition: {self.definition}"

class FlashcardApp:
    def __init__(self):
        self.flashcards = []

    def add_flashcard(self, term, definition):
        self.flashcards.append(Flashcard(term, definition))

    def review_flashcards(self):
        for flashcard in self.flashcards:
            input(f"Term: {flashcard.term}. Press Enter to see the definition...")
            print(f"Definition: {flashcard.definition}")

def main():
    app = FlashcardApp()
    while True:
        print("\n1. Add Flashcard")
        print("2. Review Flashcards")
        print("3. Quit")

        choice = input("Enter your choice: ")
        if choice == '3':
            break
        elif choice == '1':
            term = input("Enter term: ")
            definition = input("Enter definition: ")
            app.add_flashcard(term, definition)
        elif choice == '2':
            app.review_flashcards()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
