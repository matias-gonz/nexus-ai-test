import pytest

from stack import Stack  # Assuming the Stack class is in stack.py


def test_push():
    stack = Stack()
    stack.push(1)
    assert stack.size() == 1


def test_pop():
    stack = Stack()
    stack.push(1)
    assert stack.pop() == 1
    assert stack.size() == 0



def test_pop_empty():
    stack = Stack()
    with pytest.raises(Exception):
        stack.pop()



def test_peek():
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 1
    assert stack.size() == 1



def test_peek_empty():
    stack = Stack()
    with pytest.raises(Exception):
        stack.peek()



def test_is_empty():
    stack = Stack()
    assert stack.isEmpty() == True
    stack.push(1)
    assert stack.isEmpty() == False



def test_size():
    stack = Stack()
    assert stack.size() == 0
    stack.push(1)
    assert stack.size() == 1
