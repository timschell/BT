def hex_to_decimal(hex_str):
    return int(hex_str, 16)

def main():
    hex_str = input("Enter a hexadecimal number: ")
    print(f"Decimal value: {hex_to_decimal(hex_str)}")

if __name__ == "__main__":
    main()
