def bitwise_left_shift(a, n):
    return a << n

def main():
    a = int(input("Enter a number: "))
    n = int(input("Enter shift amount: "))
    print(f"Bitwise Left Shift: {bitwise_left_shift(a, n)}")

if __name__ == "__main__":
    main()
