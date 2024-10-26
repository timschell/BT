def convert_to_binary(number):
    return bin(number).replace("0b", "")

def convert_to_hexadecimal(number):
    return hex(number).replace("0x", "")

def main():
    print("Number Converter")
    number = int(input("Enter an integer: "))
    
    print(f"Binary: {convert_to_binary(number)}")
    print(f"Hexadecimal: {convert_to_hexadecimal(number)}")

if __name__ == "__main__":
    main()
