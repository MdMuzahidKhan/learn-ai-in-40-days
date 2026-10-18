# Approach: Start with the first element as the largest, then compare it with each remaining element.

def find_largest(numbers):
    if len(numbers) == 0:
        return None

    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


sample_numbers = [12, 45, 7, 89, 23]
print("Largest element:", find_largest(sample_numbers))

empty_list = []
print("Largest in empty list:", find_largest(empty_list))