def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate / (n * 100)) ** (n * time)

def main():
    print("Interest Calculator")
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (percent): "))
    time = float(input("Enter time (years): "))
    interest_type = input("Enter interest type (simple/compound): ").strip().lower()

    if interest_type == 'simple':
        interest = calculate_simple_interest(principal, rate, time)
        print(f"Simple Interest: ${interest:.2f}")
    elif interest_type == 'compound':
        n = int(input("Enter number of times interest is compounded per year: "))
        interest = calculate_compound_interest(principal, rate, time, n)
        print(f"Compound Interest: ${interest:.2f}")
    else:
        print("Invalid interest type.")

if __name__ == "__main__":
    main()
