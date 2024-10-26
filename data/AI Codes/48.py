class Expense:
    def __init__(self, description, amount, participants):
        self.description = description
        self.amount = amount
        self.participants = participants

    def __str__(self):
        return f"{self.description}: ${self.amount} split among {', '.join(self.participants)}"

class ExpenseSplitter:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount, participants):
        self.expenses.append(Expense(description, amount, participants))

    def calculate_split(self):
        splits = {}
        for expense in self.expenses:
            share = expense.amount / len(expense.participants)
            for participant in expense.participants:
                if participant in splits:
                    splits[participant] += share
                else:
                    splits[participant] = share
        return splits

    def list_expenses(self):
        for expense in self.expenses:
            print(expense)

def main():
    splitter = ExpenseSplitter()
    while True:
        print("\n1. Add Expense")
        print("2. Calculate Split")
        print("3. List Expenses")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '4':
            break
        elif choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter amount: "))
            participants = input("Enter participants (comma separated): ").split(", ")
            splitter.add_expense(description, amount, participants)
        elif choice == '2':
            splits = splitter.calculate_split()
            for participant, amount in splits.items():
                print(f"{participant} owes: ${amount:.2f}")
        elif choice == '3':
            splitter.list_expenses()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
