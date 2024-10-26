class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.phone}, {self.email}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        self.contacts.append(Contact(name, phone, email))

    def list_contacts(self):
        for contact in self.contacts:
            print(contact)

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

def main():
    manager = ContactManager()
    while True:
        print("\n1. Add Contact")
        print("2. List Contacts")
        print("3. Find Contact")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '4':
            break
        elif choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            manager.add_contact(name, phone, email)
        elif choice == '2':
            manager.list_contacts()
        elif choice == '3':
            name = input("Enter name to find: ")
            contact = manager.find_contact(name)
            if contact:
                print(contact)
            else:
                print("Contact not found.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
