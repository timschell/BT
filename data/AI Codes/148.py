def cocktail_shaker_sort(arr):
    for i in range(len(arr)//2):
        swapped = False
        for j in range(1 + i, len(arr) - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                swapped = True
        if not swapped:
            break
        swapped = False
        for j in range(len(arr) - 2 - i, i - 1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def main():
    arr = list(map(int, input("Enter array: ").split()))
    cocktail_shaker_sort(arr)
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()
