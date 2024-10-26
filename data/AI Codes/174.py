def is_palindrome(s):
    return s == s[::-1]

def main():
    s = input("Enter a string: ")
    print("Palindrome" if is_palindrome(s) else "Not Palindrome")

if __name__ == "__main__":
    main()
