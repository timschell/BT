def main():
    numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
    squared_numbers = [x**2 for x in numbers]
    print("Squared numbers:", squared_numbers)

if __name__ == "__main__":
    main()