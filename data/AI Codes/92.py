import random

def play_rps(player_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def main():
    print("Rock-Paper-Scissors Game")
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if player_choice in ["rock", "paper", "scissors"]:
        result = play_rps(player_choice)
        print(result)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
