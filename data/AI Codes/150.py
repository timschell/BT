def flip(arr, i):
    start = 0
    while start < i:
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1

def find_max(arr, n):
    max_idx = 0
    for i in range(0, n):
        if arr[i] > arr[max_idx]:
            max_idx = i
    return max_idx

def pancake_sort(arr):
    n = len(arr)
    for curr_size in range(n, 1, -1):
        max_idx = find_max(arr, curr_size)
        if max_idx != curr_size-1:
            flip(arr, max_idx)
            flip(arr, curr_size-1)

def main():
    arr = list(map(int,
