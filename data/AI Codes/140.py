def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def main():
    arr = list(map(int, input("Enter array: ").split()))
    x = int(input("Enter element to search: "))
    result = linear_search(arr, x)
    print(f"Element found at index: {result}" if result != -1 else "Element not found")

if __name__ == "__main__":
    main()
