def remove_duplicates(lst):
    return list(set(lst))

def main():
    lst = [int(x) for x in input("Enter numbers separated by space: ").split()]
    print("List without duplicates:", remove_duplicates(lst))

if __name__ == "__main__":
    main()
