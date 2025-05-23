import subprocess
import unittest

class TestCalculatorCLI(unittest.TestCase):

    def test_addition(self):
        result = subprocess.run(['python', 'calculator.py', '5', '+', '3'], capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), '8.0')

    def test_subtraction(self):
        result = subprocess.run(['python', 'calculator.py', '10', '-', '4'], capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), '6.0')

    def test_decimal_addition(self):
        result = subprocess.run(['python', 'calculator.py', '2.5', '+', '3.5'], capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), '6.0')

    def test_decimal_subtraction(self):
        result = subprocess.run(['python', 'calculator.py', '5.5', '-', '2.5'], capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), '3.0')

    def test_invalid_input(self):
        result = subprocess.run(['python', 'calculator.py', 'a', '+', 'b'], capture_output=True, text=True)
        self.assertIn('ValueError', result.stderr)

if __name__ == '__main__':
    unittest.main()
