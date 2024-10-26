from datetime import datetime

def calculate_age(birthdate):
    today = datetime.now()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def main():
    print("Age Calculator")
    birthdate = input("Enter birthdate (YYYY-MM-DD): ")
    age = calculate_age(birthdate)
    print(f"Your age is: {age} years")

if __name__ == "__main__":
    main()
