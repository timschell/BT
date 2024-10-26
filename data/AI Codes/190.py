def average(lst):
    return sum(lst) / len(lst) if lst else 0

def main():
    lst = [int(x) for x in input("Enter numbers separated by space: ").split()]
    print("Average:", average(lst))

if __name__ == "__main__":
    main()
