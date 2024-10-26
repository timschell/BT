def decimal_to_hex(n):
    return hex(n).replace("0x", "")

def main():
    n = int(input("Enter a decimal number: "))
    print(f"Hexadecimal value: {decimal_to_hex(n)}")

if __name__ == "__main__":
    main()
