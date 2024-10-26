def find_largest(numbers):
    return max(numbers)

def main():
    numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
    print("Largest number:", find_largest(numbers))

if __name__ == "__main__":
    main()
