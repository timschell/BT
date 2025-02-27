def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def main():
    text = input("Enter text: ")
    shift = int(input("Enter shift value: "))
    print(caesar_cipher(text, shift))

if __name__ == "__main__":
    main()
