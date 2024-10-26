class PasswordEntry:
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password

    def __str__(self):
        return f"{self.website} - {self.username}"

class PasswordManager:
    def __init__(self):
        self.entries = []

    def add_entry(self, website, username, password):
        self.entries.append(PasswordEntry(website, username, password))

    def list_entries(self):
        for entry in self.entries:
            print(entry)

    def find_entry(self, website):
        for entry in self.entries:
            if entry.website == website:
                return entry
        return None

def main():
    manager = PasswordManager()
    while True:
        print("\n1. Add Password Entry")
        print("2. List Password Entries")
        print("3. Find Password Entry")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '4':
            break
        elif choice == '1':
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            manager.add_entry(website, username, password)
        elif choice == '2':
            manager.list_entries()
        elif choice == '3':
            website = input("Enter website to find: ")
            entry = manager.find_entry(website)
            if entry:
                print(f"Password for {entry.website}: {entry.password}")
            else:
                print("Entry not found.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
