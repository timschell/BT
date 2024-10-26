def find_min_max(lst):
    return min(lst), max(lst)

def main():
    lst = [int(x) for x in input("Enter list of numbers separated by space: ").split()]
    min_val, max_val = find_min_max(lst)
    print("Minimum:", min_val)
    print("Maximum:", max_val)

if __name__ == "__main__":
    main()
