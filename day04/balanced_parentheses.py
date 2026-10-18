# Approach: Use a stack to track opening brackets and match them correctly with closing brackets.

from stack import Stack


def is_balanced(expression):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            top_item = stack.pop()
            if top_item is None or top_item != pairs[char]:
                return False

    return stack.is_empty()


test_1 = "{[()]}"
test_2 = "{[(])}"
test_3 = "((()))"
test_4 = "([)]"

print(test_1, "->", is_balanced(test_1))
print(test_2, "->", is_balanced(test_2))
print(test_3, "->", is_balanced(test_3))
print(test_4, "->", is_balanced(test_4))