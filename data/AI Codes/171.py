def check_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    number = int(input("Enter a number: "))
    print("The number is", check_even_or_odd(number))

if __name__ == "__main__":
    main()
