def calculate_monthly_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 100 / 12
    num_payments = years * 12
    return principal * monthly_rate / (1 - (1 + monthly_rate) ** -num_payments)

def main():
    print("Loan Calculator")
    principal = float(input("Enter loan amount: "))
    annual_rate = float(input("Enter annual interest rate (percent): "))
    years = int(input("Enter number of years: "))
    
    monthly_payment = calculate_monthly_payment(principal, annual_rate, years)
    print(f"Monthly payment: ${monthly_payment:.2f}")

if __name__ == "__main__":
    main()
