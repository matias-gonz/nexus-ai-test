import unittest

class TestStack(unittest.TestCase):

    def test_push(self):
        # Assuming there's a Stack class with push, pop, and is_empty methods
        # and that it is accessible in the current context
        stack = Stack()
        stack.push(1)
        self.assertFalse(stack.is_empty())

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.is_empty())

    def test_pop_empty_stack(self):
        stack = Stack()
        self.assertIsNone(stack.pop())

    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())

if __name__ == '__main__':
    unittest.main()
