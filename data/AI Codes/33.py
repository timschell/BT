class BudgetPlanner:
    def __init__(self):
        self.incomes = []
        self.expenses = []

    def add_income(self, description, amount):
        self.incomes.append((description, amount))

    def add_expense(self, description, amount):
        self.expenses.append((description, amount))

    def calculate_balance(self):
        total_income = sum(amount for _, amount in self.incomes)
        total_expenses = sum(amount for _, amount in self.expenses)
        return total_income - total_expenses

    def list_incomes_and_expenses(self):
        print("Incomes:")
        for description, amount in self.incomes:
            print(f"{description}: ${amount}")
        print("Expenses:")
        for description, amount in self.expenses:
            print(f"{description}: ${amount}")

def main():
    planner = BudgetPlanner()
    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Balance")
        print("4. List Incomes and Expenses")
        print("5. Quit")

        choice = input("Enter your choice: ")
        if choice == '5':
            break
        elif choice == '1':
            description = input("Enter income description: ")
            amount = float(input("Enter amount: "))
            planner.add_income(description, amount)
        elif choice == '2':
            description = input("Enter expense description: ")
            amount = float(input("Enter amount: "))
            planner.add_expense(description, amount)
        elif choice == '3':
            print(f"Current balance: ${planner.calculate_balance()}")
        elif choice == '4':
            planner.list_incomes_and_expenses()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
