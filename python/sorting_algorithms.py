import time
import random
import sys

# Increase recursion depth for Quick Sort and Merge Sort on large arrays
sys.setrecursionlimit(2000000)


# --- 1. Quadratic-Time Algorithms ---
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# --- 2. Sub-quadratic and O(n log n) Algorithms ---
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# --- 3. Linear-Time Algorithms ---
def counting_sort(arr):
    if not arr: return
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


def counting_sort_for_radix(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radix_sort(arr):
    if not arr: return
    max1 = max(arr)
    exp = 1
    while max1 / exp >= 1:
        counting_sort_for_radix(arr, exp)
        exp *= 10


# --- Benchmark Runner ---
algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Shell Sort": shell_sort,
    "Merge Sort": merge_sort,
    "Heap Sort": heap_sort,
    "Quick Sort": quick_sort,
    "Counting Sort": counting_sort,
    "Radix Sort": radix_sort
}

sizes = [100, 1000, 10000, 50000, 100000, 500000, 1000000, 1000000000]#, 10000000000]

print(f"{'Algorithm':<18} | " + " | ".join([f"N={s:<7}" for s in sizes]))
print("-" * 75)

for name, func in algorithms.items():
    times = []
    for size in sizes:
        # Safety limit for O(n^2) algorithms to prevent hours of hanging
        if size >= 100000 and name in ["Bubble Sort", "Insertion Sort", "Selection Sort"]:
            times.append("Skipped (Too Slow)")
            continue

        # Generate random array for this size
        arr = [random.randint(0, size) for _ in range(size)]

        start_time = time.perf_counter()

        # Quick Sort in this implementation returns a new array, others are in-place
        if name == "Quick Sort":
            func(arr)
        else:
            func(arr.copy())  # Copy to ensure we don't pass an already sorted array

        end_time = time.perf_counter()

        elapsed = end_time - start_time
        times.append(f"{elapsed:.5f}s")

    print(f"{name:<18} | " + " | ".join([f"{t:<9}" for t in times]))
