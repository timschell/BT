def convert_currency(amount, rate):
    return amount * rate

def main():
    print("Currency Converter")
    amount = float(input("Enter amount: "))
    rate = float(input("Enter conversion rate: "))
    converted_amount = convert_currency(amount, rate)
    print(f"Converted amount: {converted_amount}")

if __name__ == "__main__":
    main()
