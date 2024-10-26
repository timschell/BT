def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

def main():
    lst1 = [int(x) for x in input("Enter first list of numbers separated by space: ").split()]
    lst2 = [int(x) for x in input("Enter second list of numbers separated by space: ").split()]
    print("Common elements:", common_elements(lst1, lst2))

if __name__ == "__main__":
    main()
