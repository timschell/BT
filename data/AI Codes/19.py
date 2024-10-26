class UnitConverter:
    def __init__(self):
        self.conversion_factors = {
            "miles_to_km": 1.60934,
            "km_to_miles": 0.621371,
            "lbs_to_kg": 0.453592,
            "kg_to_lbs": 2.20462
        }

    def convert(self, value, conversion):
        if conversion in self.conversion_factors:
            return value * self.conversion_factors[conversion]
        else:
            return "Invalid conversion type."

def main():
    converter = UnitConverter()
    while True:
        print("\n1. Miles to Kilometers")
        print("2. Kilometers to Miles")
        print("3. Pounds to Kilograms")
        print("4. Kilograms to Pounds")
        print("5. Quit")

        choice = input("Enter your choice: ")
        if choice == '5':
            break
        value = float(input("Enter value to convert: "))
        
        if choice == '1':
            print(f"{value} miles is {converter.convert(value, 'miles_to_km')} km")
        elif choice == '2':
            print(f"{value} km is {converter.convert(value, 'km_to_miles')} miles")
        elif choice == '3':
            print(f"{value} lbs is {converter.convert(value, 'lbs_to_kg')} kg")
        elif choice == '4':
            print(f"{value} kg is {converter.convert(value, 'kg_to_lbs')} lbs")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
