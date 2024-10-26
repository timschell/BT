class Budget:
    def __init__(self):
        self.income = 0
        self.expenses = []

    def add_income(self, amount):
        self.income += amount

    def add_expense(self, description, amount):
        self.expenses.append((description, amount))

    def calculate_balance(self):
        total_expenses = sum(amount for _, amount in self.expenses)
        return self.income - total_expenses

    def list_expenses(self):
        for description, amount in self.expenses:
            print(f"{description}: ${amount}")
        print(f"Total expenses: ${sum(amount for _, amount in self.expenses)}")

def main():
    budget = Budget()
    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Balance")
        print("4. List Expenses")
        print("5. Quit")

        choice = input("Enter your choice: ")
        if choice == '5':
            break
        elif choice == '1':
            amount = float(input("Enter income amount: "))
            budget.add_income(amount)
        elif choice == '2':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            budget.add_expense(description, amount)
        elif choice == '3':
            print(f"Current balance: ${budget.calculate_balance()}")
        elif choice == '4':
            budget.list_expenses()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
