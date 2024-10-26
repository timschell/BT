class Expense:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"{self.description}: ${self.amount}"

class ExpenseLogger:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount):
        self.expenses.append(Expense(description, amount))

    def list_expenses(self):
        for expense in self.expenses:
            print(expense)

    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

def main():
    logger = ExpenseLogger()
    while True:
        print("\n1. Add Expense")
        print("2. List Expenses")
        print("3. Total Expenses")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '4':
            break
        elif choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter amount: "))
            logger.add_expense(description, amount)
        elif choice == '2':
            logger.list_expenses()
        elif choice == '3':
            print(f"Total expenses: ${logger.total_expenses()}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
