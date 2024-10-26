import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    if not re.search(r"[A-Z]", password):
        return "Weak"
    if not re.search(r"[a-z]", password):
        return "Weak"
    if not re.search(r"[0-9]", password):
        return "Weak"
    if not re.search(r"[!@#$%^&*()_+=-]", password):
        return "Weak"
    return "Strong"

def main():
    print("Password Strength Checker")
    password = input("Enter a password: ")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()
