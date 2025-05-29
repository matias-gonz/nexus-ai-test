import pytest

from stack import Stack


def test_push():
    stack = Stack()
    stack.push(1)
    assert not stack.is_empty()
    stack.push(2)
    assert stack._items == [1, 2]


def test_is_empty():
    stack = Stack()
    assert stack.is_empty()
    stack.push(1)
    assert not stack.is_empty()
    stack.pop()
    assert stack.is_empty()


def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty()


def test_pop_empty_stack():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()
