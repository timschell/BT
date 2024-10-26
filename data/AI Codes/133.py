def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def main():
    binary_str = input("Enter a binary number: ")
    print(f"Decimal value: {binary_to_decimal(binary_str)}")

if __name__ == "__main__":
    main()
