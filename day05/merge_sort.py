# Approach: Divide the list into smaller halves, sort each half recursively, then merge them.

def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers[:]

    middle = len(numbers) // 2
    left_half = merge_sort(numbers[:middle])
    right_half = merge_sort(numbers[middle:])

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


if __name__ == "__main__":
    sample_numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", sample_numbers)
    print("Sorted list:", merge_sort(sample_numbers))