class PyStack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.isEmpty():
            raise Exception("Cannot pop from an empty stack.")
        return self._data.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Cannot peek into an empty stack.")
        return self._data[-1]

    def isEmpty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)


# Example usage:
if __name__ == '__main__':
    stack = PyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack size:", stack.size())
    print("Stack peek:", stack.peek())

    print("Popped:", stack.pop())
    print("Popped:", stack.pop())

    print("Stack size after pops:", stack.size())
    print("Stack peek:", stack.peek())

    print("Popped:", stack.pop())

    print("Stack is empty:", stack.isEmpty())

    try:
        stack.pop()
    except Exception as e:
        print(e)

    try:
        stack.peek()
    except Exception as e:
        print(e)
