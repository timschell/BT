def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

def main():
    n = int(input("Enter a number: "))
    print(f"{n} is a palindrome." if is_palindrome_number(n) else f"{n} is not a palindrome.")

if __name__ == "__main__":
    main()
