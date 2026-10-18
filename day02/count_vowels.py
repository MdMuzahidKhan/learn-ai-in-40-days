# Approach: Convert the sentence to lowercase and count characters that are vowels.

def count_vowels(sentence):
    vowels = "aeiou"
    count = 0

    for character in sentence.lower():
        if character in vowels:
            count += 1

    return count


sample_sentence = "Hello World"
print("Vowel count:", count_vowels(sample_sentence))

another_sentence = "PYTHON programming"
print("Vowel count:", count_vowels(another_sentence))