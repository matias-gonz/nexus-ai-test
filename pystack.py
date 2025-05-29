class PyStack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.isEmpty():
            raise Exception("Cannot pop from an empty stack")
        return self._items.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Cannot peek into an empty stack")
        return self._items[-1]

    def isEmpty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

# Example Usage:
if __name__ == '__main__':
    stack = PyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack size:", stack.size())
    print("Stack is empty:", stack.isEmpty())
    print("Peek:", stack.peek())
    print("Pop:", stack.pop())
    print("Peek:", stack.peek())
    print("Stack size:", stack.size())

    try:
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
    except Exception as e:
        print(e)

    try:
        stack.peek()
    except Exception as e:
        print(e)
