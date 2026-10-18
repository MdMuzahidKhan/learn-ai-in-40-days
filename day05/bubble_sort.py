# Approach: Repeatedly compare adjacent elements and swap them until the list is sorted.

def bubble_sort(numbers):
    sorted_numbers = numbers[:]
    length = len(sorted_numbers)

    for i in range(length):
        for j in range(0, length - i - 1):
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                sorted_numbers[j], sorted_numbers[j + 1] = sorted_numbers[j + 1], sorted_numbers[j]

    return sorted_numbers


if __name__ == "__main__":
    sample_numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", sample_numbers)
    print("Sorted list:", bubble_sort(sample_numbers))