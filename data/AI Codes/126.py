def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

def main():
    n = int(input("Enter a number: "))
    print(f"{n} is a Fibonacci number." if is_fibonacci(n) else f"{n} is not a Fibonacci number.")

if __name__ == "__main__":
    main()
