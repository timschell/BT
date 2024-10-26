def binary_to_hex(binary_str):
    return hex(int(binary_str, 2)).replace("0x", "")

def main():
    binary_str = input("Enter a binary number: ")
    print(f"Hexadecimal value: {binary_to_hex(binary_str)}")

if __name__ == "__main__":
    main()
