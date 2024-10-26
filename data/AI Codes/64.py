def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Converter")
    while True:
        print("\n1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Quit")

        choice = input("Enter your choice: ")
        if choice == '3':
            break
        elif choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(celsius):.2f}°F")
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"Temperature in Celsius: {fahrenheit_to_celsius(fahrenheit):.2f}°C")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
