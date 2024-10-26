def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def main():
    n = int(input("Enter number of Fibonacci terms: "))
    print(fibonacci(n))

if __name__ == "__main__":
    main()
