def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def main():
    arr = list(map(int, input("Enter array: ").split()))
    shell_sort(arr)
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()
