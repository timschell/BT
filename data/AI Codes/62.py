class Address:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} - {self.phone}, {self.email}, {self.address}"

class AddressBook:
    def __init__(self):
        self.entries = []

    def add_entry(self, name, phone, email, address):
        self.entries.append(Address(name, phone, email, address))

    def list_entries(self):
        for entry in self.entries:
            print(entry)

    def find_entry(self, name):
        for entry in self.entries:
            if entry.name == name:
                return entry
        return None

def main():
    book = AddressBook()
    while True:
        print("\n1. Add Address")
        print("2. List Addresses")
        print("3. Find Address")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '4':
            break
        elif choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter physical address: ")
            book.add_entry(name, phone, email, address)
        elif choice == '2':
            book.list_entries()
        elif choice == '3':
            name = input("Enter name to find: ")
            entry = book.find_entry(name)
            if entry:
                print(entry)
            else:
                print("Address not found.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
