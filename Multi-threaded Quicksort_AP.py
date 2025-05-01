import threading
import time
import random
import sys

sys.setrecursionlimit(100000)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = quicksort([x for x in arr[1:] if x <= pivot])
    right = quicksort([x for x in arr[1:] if x > pivot])
    return left + [pivot] + right

def threaded_quicksort(arr, result, index):
    result[index] = quicksort(arr)

def multi_threaded_quicksort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    result = [None, None]

    t1 = threading.Thread(target=threaded_quicksort, args=(arr[:mid], result, 0))
    t2 = threading.Thread(target=threaded_quicksort, args=(arr[mid:], result, 1))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    return quicksort(result[0] + result[1])

# Example
if __name__ == "__main__":
    arr = [random.randint(0, 10000) for _ in range(100000)]
    start = time.time()
    sorted_single = quicksort(arr)
    print("Single-threaded time:", time.time() - start)

    start = time.time()
    sorted_multi = multi_threaded_quicksort(arr)
    print("Multi-threaded time:", time.time() - start)
