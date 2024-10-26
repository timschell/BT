import random

def get_random_quote():
    quotes = [
        "The greatest glory in living lies not in never falling, but in rising every time we fall.",
        "The way to get started is to quit talking and begin doing.",
        "Life is what happens when you're busy making other plans.",
        "The future belongs to those who believe in the beauty of their dreams.",
        "In the end, we will remember not the words of our enemies, but the silence of our friends."
    ]
    return random.choice(quotes)

def main():
    print("Random Quote Generator")
    print(f"Quote: {get_random_quote()}")

if __name__ == "__main__":
    main()
