class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return f"{self.title}: {self.content}"

class NoteTakingApp:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content):
        self.notes.append(Note(title, content))

    def list_notes(self):
        for note in self.notes:
            print(note)

    def delete_note(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                print("Note deleted.")
                return
        print("Note not found.")

def main():
    app = NoteTakingApp()
    while True:
        print("\n1. Add Note")
        print("2. List Notes")
        print("3. Delete Note")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '4':
            break
        elif choice == '1':
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            app.add_note(title, content)
        elif choice == '2':
            app.list_notes()
        elif choice == '3':
            title = input("Enter note title to delete: ")
            app.delete_note(title)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
