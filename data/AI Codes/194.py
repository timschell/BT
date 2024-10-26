from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def main():
    date_str = input("Enter a date (YYYY-MM-DD): ")
    print("Valid date" if validate_date(date_str) else "Invalid date")

if __name__ == "__main__":
    main()
