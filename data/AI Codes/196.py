def merge_lists(lst1, lst2):
    return lst1 + lst2

def main():
    lst1 = [int(x) for x in input("Enter first list of numbers separated by space: ").split()]
    lst2 = [int(x) for x in input("Enter second list of numbers separated by space: ").split()]
    print("Merged list:", merge_lists(lst1, lst2))

if __name__ == "__main__":
    main()
