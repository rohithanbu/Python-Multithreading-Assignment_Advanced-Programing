import threading
import time
import random

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def threaded_merge_sort(arr, result, index):
    result[index] = merge_sort(arr)

def multi_threaded_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    result = [None, None]
    
    t1 = threading.Thread(target=threaded_merge_sort, args=(arr[:mid], result, 0))
    t2 = threading.Thread(target=threaded_merge_sort, args=(arr[mid:], result, 1))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    return merge(result[0], result[1])

# Example
if __name__ == "__main__":
    arr = [random.randint(0, 10000) for _ in range(100000)]
    start = time.time()
    sorted_single = merge_sort(arr)
    print("Single-threaded time:", time.time() - start)

    start = time.time()
    sorted_multi = multi_threaded_merge_sort(arr)
    print("Multi-threaded time:", time.time() - start)
