class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {self.quantity}"

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity):
        for item in self.items:
            if item.name == name:
                item.quantity += quantity
                return
        self.items.append(Item(name, quantity))

    def list_items(self):
        for item in self.items:
            print(item)

def main():
    inventory = Inventory()
    while True:
        print("\n1. Add Item")
        print("2. List Items")
        print("3. Quit")

        choice = input("Enter your choice: ")
        if choice == '3':
            break
        elif choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            inventory.add_item(name, quantity)
        elif choice == '2':
            inventory.list_items()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
