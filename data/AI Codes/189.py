def main():
    lst = [int(x) for x in input("Enter numbers separated by space: ").split()]
    lst.sort()
    print("Sorted list:", lst)

if __name__ == "__main__":
    main()
