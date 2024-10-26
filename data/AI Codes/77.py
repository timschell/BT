def encrypt(text, key):
    return ''.join(chr(ord(c) + key) for c in text)

def decrypt(text, key):
    return ''.join(chr(ord(c) - key) for c in text)

def main():
    print("Encryption/Decryption Tool")
    choice = input("1. Encrypt\n2. Decrypt\nChoose an option: ")
    text = input("Enter text: ")
    key = int(input("Enter key (integer): "))
    
    if choice == '1':
        encrypted_text = encrypt(text, key)
        print(f"Encrypted text: {encrypted_text}")
    elif choice == '2':
        decrypted_text = decrypt(text, key)
        print(f"Decrypted text: {decrypted_text}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
