def compare_and_swap(arr, i, j, dir):
    if (dir == 1 and arr[i] > arr[j]) or (dir == 0 and arr[i] < arr[j]):
        arr[i], arr[j] = arr[j], arr[i]

def bitonic_merge(arr, low, cnt, dir):
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            compare_and_swap(arr, i, i + k, dir)
        bitonic_merge(arr, low, k, dir)
        bitonic_merge(arr, low + k, k, dir)

def bitonic_sort(arr, low, cnt, dir):
    if cnt > 1:
        k = cnt // 2
        bitonic_sort(arr, low, k, 1)
        bitonic_sort(arr, low + k, k, 0)
        bitonic_merge(arr, low, cnt, dir)

def sort(arr, n, up):
    bitonic_sort(arr, 0, n, up)

def main():
    arr = list(map(int, input("Enter array: ").split()))
    n = len(arr)
    up = 1
    sort(arr, n, up)
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()
