# Approach: Implement a custom stack using a list and allow push, pop, peek, and size operations.

class Stack:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if self.is_empty():
			return None
		return self.items.pop()

	def peek(self):
		if self.is_empty():
			return None
		return self.items[-1]

	def is_empty(self):
		return len(self.items) == 0

	def size(self):
		return len(self.items)


if __name__ == "__main__":
	stack = Stack()
	stack.push(10)
	stack.push(20)
	stack.push(30)

	print("Top item:", stack.peek())
	print("Popped item:", stack.pop())
	print("Current size:", stack.size())