import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    while True:
        player_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
        if player_choice == 'exit':
            break
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    main()
