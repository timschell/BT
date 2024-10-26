class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        self.contacts.append(Contact(name, phone, email))

    def list_contacts(self):
        for contact in self.contacts:
            print(contact)

def main():
    book = ContactBook()
    while True:
        print("\n1. Add Contact")
        print("2. List Contacts")
        print("3. Quit")

        choice = input("Enter your choice: ")
        if choice == '3':
            break
        elif choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            book.add_contact(name, phone, email)
        elif choice == '2':
            book.list_contacts()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
