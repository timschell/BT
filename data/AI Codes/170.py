def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def main():
    arr = list(map(int, raw_input("Enter array: ").split()))
    selection_sort(arr)
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()
