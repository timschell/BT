def bitwise_right_shift(a, n):
    return a >> n

def main():
    a = int(input("Enter a number: "))
    n = int(input("Enter shift amount: "))
    print(f"Bitwise Right Shift: {bitwise_right_shift(a, n)}")

if __name__ == "__main__":
    main()
