def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    print("Binary Search")
    arr = list(map(int, input("Enter sorted numbers (comma separated): ").split(", ")))
    target = int(input("Enter number to search for: "))
    result = binary_search(arr, target)
    if result != -1:
        print(f"Number found at index {result}.")
    else:
        print("Number not found.")

if __name__ == "__main__":
    main()
