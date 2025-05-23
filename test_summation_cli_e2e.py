import subprocess
import unittest

class TestSummationCLI(unittest.TestCase):

    def test_valid_input(self):
        process = subprocess.run(['python', 'summation_cli.py', '5', '10'], capture_output=True, text=True)
        self.assertEqual(process.returncode, 0)
        self.assertEqual(process.stdout.strip(), '15')

    def test_invalid_input(self):
        process = subprocess.run(['python', 'summation_cli.py', '5', 'a'], capture_output=True, text=True)
        self.assertEqual(process.returncode, 1) # Assuming the CLI returns 1 for invalid input
        self.assertIn('invalid input', process.stderr.lower())

    def test_no_input(self):
        process = subprocess.run(['python', 'summation_cli.py'], capture_output=True, text=True)
        self.assertEqual(process.returncode, 2)
        self.assertIn('error: the following arguments are required: num1, num2', process.stderr)

if __name__ == '__main__':
    unittest.main()
