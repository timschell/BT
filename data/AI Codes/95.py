def decimal_to_hexadecimal(n):
    return hex(n).replace("0x", "")

def main():
    print("Decimal to Hexadecimal Converter")
    decimal_number = int(input("Enter a decimal number: "))
    hexadecimal_number = decimal_to_hexadecimal(decimal_number)
    print(f"Hexadecimal representation: {hexadecimal_number}")

if __name__ == "__main__":
    main()
