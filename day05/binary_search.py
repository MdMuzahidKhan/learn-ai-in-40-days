# Approach: Use the middle element to repeatedly cut the search space in half.

def binary_search_iterative(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def binary_search_recursive(numbers, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2

    if numbers[middle] == target:
        return middle
    if numbers[middle] < target:
        return binary_search_recursive(numbers, target, middle + 1, right)
    return binary_search_recursive(numbers, target, left, middle - 1)


if __name__ == "__main__":
    sorted_numbers = [3, 7, 12, 18, 25, 31, 42, 56]
    target = 25

    print("Sorted list:", sorted_numbers)
    print("Target:", target)
    print("Iterative result index:", binary_search_iterative(sorted_numbers, target))
    print(
        "Recursive result index:",
        binary_search_recursive(sorted_numbers, target, 0, len(sorted_numbers) - 1),
    )