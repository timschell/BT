def encrypt_text(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

def decrypt_text(text, shift):
    return encrypt_text(text, -shift)

def main():
    print("Text Encryption and Decryption")
    text = input("Enter text: ")
    shift = int(input("Enter shift value: "))
    encrypted_text = encrypt_text(text, shift)
    print(f"Encrypted text: {encrypted_text}")
    decrypted_text = decrypt_text(encrypted_text, shift)
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
