import random

def main():
    number = random.randint(1, 10)
    guess = int(input("Guess the number (between 1 and 10): "))
    
    if guess == number:
        print("Congratulations! You guessed correctly.")
    else:
        print("Sorry, the number was", number)

if __name__ == "__main__":
    main()
