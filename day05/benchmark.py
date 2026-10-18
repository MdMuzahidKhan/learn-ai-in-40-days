# Approach: Generate the same random data for both algorithms, time them, and compare the results.

import random
import time
from bubble_sort import bubble_sort
from merge_sort import merge_sort


def time_algorithm(sort_function, numbers):
    start_time = time.perf_counter()
    sort_function(numbers)
    end_time = time.perf_counter()
    return end_time - start_time


def run_benchmark():
    sizes = [100, 1000, 10000]

    print("Sorting Benchmark")
    print("-" * 50)
    print(f"{'Size':<10}{'Bubble Sort (s)':<20}{'Merge Sort (s)':<20}")
    print("-" * 50)

    for size in sizes:
        numbers = [random.randint(1, 100000) for _ in range(size)]

        bubble_time = time_algorithm(bubble_sort, numbers[:])
        merge_time = time_algorithm(merge_sort, numbers[:])

        print(f"{size:<10}{bubble_time:<20.6f}{merge_time:<20.6f}")


if __name__ == "__main__":
    run_benchmark()