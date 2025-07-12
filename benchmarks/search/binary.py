from time import perf_counter_ns as top


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1


def main():
    n = 1_000_000

    arr = []
    for i in range(n):
        arr.append(i)

    t = top()

    results = []
    for i in range(n):
        results.append(binary_search(arr, i))

    print(round((top() - t) / 1e9, 3), "s")
    print("Results: ", len(results))


main()
