from datetime import datetime

def format_date(date_str, format_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        return date.strftime(format_str)
    except ValueError:
        return "Invalid date format."

def main():
    print("Date Formatter")
    date_str = input("Enter date (YYYY-MM-DD): ")
    format_str = input("Enter format string (e.g., %d-%m-%Y): ")
    formatted_date = format_date(date_str, format_str)
    print(f"Formatted date: {formatted_date}")

if __name__ == "__main__":
    main()
