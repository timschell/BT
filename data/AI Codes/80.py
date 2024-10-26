import random

def roll_dice(num_sides):
    return random.randint(1, num_sides)

def main():
    print("Dice Roller")
    num_sides = int(input("Enter the number of sides on the dice: "))
    result = roll_dice(num_sides)
    print(f"You rolled a {result}")

if __name__ == "__main__":
    main()
