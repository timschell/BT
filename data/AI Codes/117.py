def count_number_frequency(numbers):
    frequency = {}
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    return frequency

def main():
    print("Number Frequency Counter")
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    frequency = count_number_frequency(numbers)
    for number, count in frequency.items():
        print(f"{number}: {count}")

if __name__ == "__main__":
    main()
