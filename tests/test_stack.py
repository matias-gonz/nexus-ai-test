import pytest

from stack import Stack  # Assuming the stack implementation is in stack.py


def test_push():
    stack = Stack()
    stack.push(1)
    assert not stack.is_empty()


def test_pop():
    stack = Stack()
    stack.push(1)
    assert stack.pop() == 1
    assert stack.is_empty()


def test_pop_empty():
    stack = Stack()
    with pytest.raises(Exception):
        stack.pop()


def test_is_empty():
    stack = Stack()
    assert stack.is_empty()
    stack.push(1)
    assert not stack.is_empty()