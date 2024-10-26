def convert_length(meters):
    return meters * 3.28084

def convert_weight(kilograms):
    return kilograms * 2.20462

def main():
    print("Unit Converter")
    while True:
        print("\n1. Convert Length (meters to feet)")
        print("2. Convert Weight (kilograms to pounds)")
        print("3. Quit")

        choice = input("Enter your choice: ")
        if choice == '3':
            break
        elif choice == '1':
            meters = float(input("Enter length in meters: "))
            feet = convert_length(meters)
            print(f"{meters} meters is {feet:.2f} feet")
        elif choice == '2':
            kilograms = float(input("Enter weight in kilograms: "))
            pounds = convert_weight(kilograms)
            print(f"{kilograms} kilograms is {pounds:.2f} pounds")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
