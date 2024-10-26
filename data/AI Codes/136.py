def hex_to_binary(hex_str):
    return bin(int(hex_str, 16)).replace("0b", "")

def main():
    hex_str = input("Enter a hexadecimal number: ")
    print(f"Binary value: {hex_to_binary(hex_str)}")

if __name__ == "__main__":
    main()
