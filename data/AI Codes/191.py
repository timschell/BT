def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def main():
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (in %): "))
    time = float(input("Enter time (in years): "))
    print("Simple Interest:", simple_interest(principal, rate, time))

if __name__ == "__main__":
    main()
