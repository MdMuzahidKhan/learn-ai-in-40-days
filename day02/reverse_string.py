# Approach: Build the reversed string manually by iterating from the end to the beginning.

def reverse_string(text):
    reversed_text = ""
    for index in range(len(text) - 1, -1, -1):
        reversed_text += text[index]
    return reversed_text


sample_text = "Python"
print("Original:", sample_text)
print("Reversed:", reverse_string(sample_text))

empty_text = ""
print("Empty string reversed:", reverse_string(empty_text))