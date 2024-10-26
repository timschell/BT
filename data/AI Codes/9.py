import random

class SimpleChatBot:
    def __init__(self):
        self.greetings = ["Hello!", "Hi there!", "Greetings!", "Howdy!", "Hey!"]
        self.farewells = ["Goodbye!", "See you later!", "Take care!", "Bye!", "Farewell!"]

    def get_greeting(self):
        return random.choice(self.greetings)

    def get_farewell(self):
        return random.choice(self.farewells)

    def respond_to_query(self, query):
        responses = {
            "how are you": "I'm just a bunch of code, but I'm functioning as expected!",
            "what is your name": "I am a simple chatbot.",
            "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        }
        return responses.get(query.lower(), "I don't understand that question.")

def main():
    bot = SimpleChatBot()
    print(bot.get_greeting())
    while True:
        query = input("You: ")
        if query.lower() in ["bye", "exit", "quit"]:
            print(bot.get_farewell())
            break
        else:
            print(f"Bot: {bot.respond_to_query(query)}")

if __name__ == "__main__":
    main()
