def counting_sort(arr):
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m

    for a in arr:
        count[a] += 1

    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1

def main():
    arr = list(map(int, input("Enter array: ").split()))
    counting_sort(arr)
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()
