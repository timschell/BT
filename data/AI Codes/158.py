def bucket_sort(arr):
    bucket = [[] for _ in range(len(arr))]

    for num in arr:
        index = int(num * len(arr))
        bucket[index].append(num)

    for i in range(len(arr)):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(len(arr)):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1

def main():
    arr = list(map(float, input("Enter array: ").split()))
    bucket_sort(arr)
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()
