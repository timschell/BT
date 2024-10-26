def calculate_bmi(weight, height):
    return weight / (height ** 2)

def main():
    print("BMI Calculator")
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")

if __name__ == "__main__":
    main()
