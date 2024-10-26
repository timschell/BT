def fibonacci(n):
    a, b = 0, 1
    sequence = []
    while a < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    n = int(input("Enter a number: "))
    print("Fibonacci sequence:", fibonacci(n))

if __name__ == "__main__":
    main()
