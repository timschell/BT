def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def main():
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    sequence = fibonacci(n)
    for i, num in enumerate(sequence):
        print(f"Fibonacci {i+1}: {num}")

if __name__ == "__main__":
    main()
