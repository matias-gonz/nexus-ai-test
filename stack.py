class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0

# Example Usage:
if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(f"Stack is empty: {stack.is_empty()}")  # Output: False
    print(f"Popped item: {stack.pop()}")  # Output: 3
    print(f"Popped item: {stack.pop()}")  # Output: 2
    print(f"Popped item: {stack.pop()}")  # Output: 1
    print(f"Stack is empty: {stack.is_empty()}")  # Output: True

    try:
        stack.pop()
    except IndexError as e:
        print(e)  # Output: pop from an empty stack
