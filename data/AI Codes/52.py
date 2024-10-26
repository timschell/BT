class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return f"Recipe: {self.name}\nIngredients: {', '.join(self.ingredients)}"

class RecipeManager:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, name, ingredients):
        self.recipes.append(Recipe(name, ingredients))

    def list_recipes(self):
        for recipe in self.recipes:
            print(recipe)

    def find_recipe(self, name):
        for recipe in self.recipes:
            if recipe.name == name:
                return recipe
        return None

def main():
    manager = RecipeManager()
    while True:
        print("\n1. Add Recipe")
        print("2. List Recipes")
        print("3. Find Recipe")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '4':
            break
        elif choice == '1':
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma separated): ").split(", ")
            manager.add_recipe(name, ingredients)
        elif choice == '2':
            manager.list_recipes()
        elif choice == '3':
            name = input("Enter recipe name to find: ")
            recipe = manager.find_recipe(name)
            if recipe:
                print(recipe)
            else:
                print("Recipe not found.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
