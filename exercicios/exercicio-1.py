import math
import random


def linear_search(arr, target):
    comparisons = 0

    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons

    return -1, comparisons


def is_sample_sorted(arr):
    n = len(arr)
    if n <= 1:
        return True

    sample_size = int(math.sqrt(n))
    indices = random.sample(range(n - 1), sample_size)

    for i in indices:
        if arr[i] > arr[i + 1]:
            return False

    return True


def binary_search(sorted_arr, target):
    if not is_sample_sorted(sorted_arr):
        raise ValueError("O array deve estar ordenado")

    comparisons = 0
    start = 0
    end = len(sorted_arr) - 1

    while start <= end:
        mid = (start + end) // 2
        comparisons += 1
        if sorted_arr[mid] == target:
            return mid, comparisons
        elif sorted_arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1, comparisons


def generate_array(n):
    return [random.randint(0, n * 10) for _ in range(n)]


scales = [100, 1000, 10_000, 100_000, 1_000_000]
print("Comparações por tipo de busca")
for n in scales:
    arr = generate_array(n)
    target = arr[n // 2]

    _, linear_comps = linear_search(arr, target)

    sorted_arr = sorted(arr)
    _, binary_comps = binary_search(sorted_arr, target)

    print(f"\nComprimento do array: {n}")
    print(f"Linear Search: {linear_comps}")
    print(f"Binary Search: {binary_comps}")


print("\nTeste com array desordenado")
try:
    unsorted_arr = [5, 3, 8, 1, 9, 2, 7]
    binary_search(unsorted_arr, 3)
    print("nenhuma exceção lançada (Falso positivo)")
except ValueError as e:
    print(f"exceção capturada: {e}")
