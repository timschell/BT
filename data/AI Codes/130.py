import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def main():
    length = int(input("Enter password length: "))
    print(f"Generated password: {generate_password(length)}")

if __name__ == "__main__":
    main()
