def add_note():
    note = input("Enter note: ")
    with open('notes.txt', 'a') as file:
        file.write(note + "\n")
    print("Note added.")

def list_notes():
    with open('notes.txt', 'r') as file:
        notes = file.readlines()
    for note in notes:
        print(note.strip())

def main():
    while True:
        print("\n1. Add Note")
        print("2. List Notes")
        print("3. Quit")

        choice = input("Enter your choice: ")
        if choice == '3':
            break
        elif choice == '1':
            add_note()
        elif choice == '2':
            list_notes()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
