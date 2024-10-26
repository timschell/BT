def convert_units(value, unit_from, unit_to):
    conversion_factors = {
        'cm_to_m': 0.01,
        'm_to_cm': 100,
        'kg_to_g': 1000,
        'g_to_kg': 0.001
    }
    key = f"{unit_from}_to_{unit_to}"
    return value * conversion_factors.get(key, 1)

def main():
    print("Unit Converter")
    value = float(input("Enter value: "))
    unit_from = input("Enter unit from (e.g., cm, m, kg, g): ")
    unit_to = input("Enter unit to (e.g., cm, m, kg, g): ")
    converted_value = convert_units(value, unit_from, unit_to)
    print(f"Converted value: {converted_value}")

if __name__ == "__main__":
    main()
