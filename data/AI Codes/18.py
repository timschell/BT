class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount):
        self.expenses.append({'description': description, 'amount': amount})

    def list_expenses(self):
        total = 0
        for expense in self.expenses:
            print(f"{expense['description']}: ${expense['amount']}")
            total += expense['amount']
        print(f"Total: ${total}")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\n1. Add Expense")
        print("2. List Expenses")
        print("3. Quit")

        choice = input("Enter your choice: ")
        if choice == '1':
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            tracker.add_expense(description, amount)
        elif choice == '2':
            tracker.list_expenses()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
