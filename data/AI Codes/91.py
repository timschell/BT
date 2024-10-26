def decimal_to_binary(n):
    return bin(n).replace("0b", "")

def main():
    print("Decimal to Binary Converter")
    decimal_number = int(input("Enter a decimal number: "))
    binary_number = decimal_to_binary(decimal_number)
    print(f"Binary representation: {binary_number}")

if __name__ == "__main__":
    main()
