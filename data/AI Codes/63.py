def convert_currency(amount, rate):
    return amount * rate

def main():
    print("Currency Converter")
    amount = float(input("Enter amount in your currency: "))
    rate = float(input("Enter exchange rate to USD: "))
    
    converted_amount = convert_currency(amount, rate)
    print(f"Amount in USD: ${converted_amount:.2f}")

if __name__ == "__main__":
    main()
