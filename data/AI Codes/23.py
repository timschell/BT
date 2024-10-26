class CurrencyConverter:
    def __init__(self):
        self.exchange_rates = {
            "USD": {"EUR": 0.85, "JPY": 110.53, "GBP": 0.73},
            "EUR": {"USD": 1.18, "JPY": 129.53, "GBP": 0.86},
            "JPY": {"USD": 0.009, "EUR": 0.0077, "GBP": 0.0066},
            "GBP": {"USD": 1.37, "EUR": 1.17, "JPY": 151.94},
        }

    def convert(self, amount, from_currency, to_currency):
        if from_currency in self.exchange_rates and to_currency in self.exchange_rates[from_currency]:
            return amount * self.exchange_rates[from_currency][to_currency]
        else:
            return "Conversion rate not available."

def main():
    converter = CurrencyConverter()
    while True:
        print("\n1. Convert Currency")
        print("2. Quit")

        choice = input("Enter your choice: ")
        if choice == '2':
            break
        elif choice == '1':
            amount = float(input("Enter amount: "))
            from_currency = input("Enter from currency (USD, EUR, JPY, GBP): ").upper()
            to_currency = input("Enter to currency (USD, EUR, JPY, GBP): ").upper()
            result = converter.convert(amount, from_currency, to_currency)
            print(f"Converted amount: {result}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
