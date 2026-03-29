import random
import time


def remove_duplicates(arr):
    seen = {}
    result = []
    for element in arr:
        if element not in seen:
            seen[element] = True
            result.append(element)
    return result


def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quickselect(arr, left, right, k):
    k -= 1
    if left <= right:
        pivot_idx = partition(arr, left, right)
        if pivot_idx == k:
            return arr[pivot_idx]
        elif pivot_idx > k:
            quickselect(arr, left, pivot_idx - 1, k + 1)
        else:
            quickselect(arr, pivot_idx + 1, right, k + 1)

    return None


def k_smallest_a(arr, k):
    sorted_arr = sorted(arr)
    return sorted_arr[:k]


def k_smallest_b(arr, k):
    quickselect(arr, 0, len(arr) - 1, k)
    return arr[:k]


def generate_array_with_duplicates(n):
    universe = n // 2
    return [random.randint(0, universe) for _ in range(n)]


sizes = [1000, 10_000, 25_000, 50_000, 100_000, 10_000_000, 25_000_000]
k = 10

print(f"{'n':<10} {'sem dupl.':<12} {'versão A (ms)':<16} {'versão B (ms)':<16}")
for n in sizes:
    arr = generate_array_with_duplicates(n)
    unique_arr = remove_duplicates(arr)
    m = len(unique_arr)

    k_real = min(k, m)

    start = time.perf_counter()
    k_smallest_a(unique_arr[:], k_real)
    time_a = (time.perf_counter() - start) * 1000

    start = time.perf_counter()
    k_smallest_b(unique_arr[:], k_real)
    time_b = (time.perf_counter() - start) * 1000

    print(f"{n:<10} {m:<12} {time_a:<16.4f} {time_b:<16.4f}")
