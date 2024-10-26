class Expense:
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category

    def __str__(self):
        return f"{self.description}: ${self.amount} ({self.category})"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount, category):
        self.expenses.append(Expense(description, amount, category))

    def list_expenses(self):
        total = 0
        for expense in self.expenses:
            print(expense)
            total += expense.amount
        print(f"Total: ${total}")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\n1. Add Expense")
        print("2. List Expenses")
        print("3. Quit")

        choice = input("Enter your choice: ")
        if choice == '3':
            break
        elif choice == '1':
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            tracker.add_expense(description, amount, category)
        elif choice == '2':
            tracker.list_expenses()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
