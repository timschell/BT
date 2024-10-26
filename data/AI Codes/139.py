def binary_search(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def main():
    arr = list(map(int, input("Enter sorted array: ").split()))
    x = int(input("Enter element to search: "))
    result = binary_search(arr, x)
    print(f"Element found at index: {result}" if result != -1 else "Element not found")

if __name__ == "__main__":
    main()
