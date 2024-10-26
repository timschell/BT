import threading

def sleep_sort(arr):
    result = []
    def sleep_and_append(x):
        threading.Event().wait(x)
        result.append(x)
    threads = [threading.Thread(target=sleep_and_append, args=(x,)) for x in arr]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return result

def main():
    arr = list(map(int, input("Enter array: ").split()))
    sorted_arr = sleep_sort(arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
