import subprocess
import unittest

class TestNumberAdder(unittest.TestCase):

    def test_addition(self):
        # Test with positive integers
        result = subprocess.run(['python', 'number_adder.py', '5', '3'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), '8')

    def test_negative_numbers(self):
        # Test with negative integers
        result = subprocess.run(['python', 'number_adder.py', '-5', '-3'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), '-8')

    def test_mixed_numbers(self):
        # Test with mixed positive and negative integers
        result = subprocess.run(['python', 'number_adder.py', '5', '-3'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), '2')

    def test_invalid_input(self):
        # Test with invalid input (non-integers)
        result = subprocess.run(['python', 'number_adder.py', 'a', 'b'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('invalid integer value', result.stderr)

    def test_missing_argument(self):
        # Test with missing argument
        result = subprocess.run(['python', 'number_adder.py', '5'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn('error: the following arguments are required: num2', result.stderr)

if __name__ == '__main__':
    unittest.main()
