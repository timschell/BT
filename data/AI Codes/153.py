def gnome_sort(arr):
    index = 0
    while index < len(arr):
        if index == 0 or arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1

def main():
    arr = list(map(int, input("Enter array: ").split()))
    gnome_sort(arr)
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()
