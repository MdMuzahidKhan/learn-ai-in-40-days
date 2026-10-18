# Approach: Implement a custom queue using a list and allow enqueue, dequeue, peek, and size operations.

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue("Job 1")
    queue.enqueue("Job 2")
    queue.enqueue("Job 3")

    print("Front item:", queue.peek())
    print("Processed item:", queue.dequeue())
    print("Current size:", queue.size())