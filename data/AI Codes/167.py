def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def main():
    arr = list(map(int, raw_input("Enter array: ").split()))
    x = int(raw_input("Enter element to search: "))
    result = linear_search(arr, x)
    if result != -1:
        print("Element found at index:", result)
    else:
        print("Element not found")

if __name__ == "__main__":
    main()
