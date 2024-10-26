def decimal_to_binary(n):
    return bin(n).replace("0b", "")

def main():
    n = int(input("Enter a decimal number: "))
    print(f"Binary value: {decimal_to_binary(n)}")

if __name__ == "__main__":
    main()
