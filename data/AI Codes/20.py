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

    def remove_item(self, name, quantity):
        for item in self.items:
            if item.name == name:
                if item.quantity >= quantity:
                    item.quantity -= quantity
                    if item.quantity == 0:
                        self.items.remove(item)
                else:
                    print("Not enough items in stock.")
                return
        print("Item not found.")

    def list_items(self):
        for item in self.items:
            print(item)

def main():
    inventory = Inventory()
    while True:
        print("\n1. Add Item")
        print("2. Remove Item")
        print("3. List Items")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '4':
            break
        elif choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            inventory.add_item(name, quantity)
        elif choice == '2':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            inventory.remove_item(name, quantity)
        elif choice == '3':
            inventory.list_items()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
