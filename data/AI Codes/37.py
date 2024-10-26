class Meal:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return f"{self.name}: {', '.join(self.ingredients)}"

class MealPlanner:
    def __init__(self):
        self.meals = []

    def add_meal(self, name, ingredients):
        self.meals.append(Meal(name, ingredients))

    def list_meals(self):
        for meal in self.meals:
            print(meal)

def main():
    planner = MealPlanner()
    while True:
        print("\n1. Add Meal")
        print("2. List Meals")
        print("3. Quit")

        choice = input("Enter your choice: ")
        if choice == '3':
            break
        elif choice == '1':
            name = input("Enter meal name: ")
            ingredients = input("Enter ingredients (comma separated): ").split(", ")
            planner.add_meal(name, ingredients)
        elif choice == '2':
            planner.list_meals()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
