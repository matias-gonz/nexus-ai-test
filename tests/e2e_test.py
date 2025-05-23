import subprocess
import unittest

class TestSumCLI(unittest.TestCase):

    def test_valid_input(self):
        result = subprocess.run(['python', 'cli.py', '2', '3'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), '5.0')

    def test_invalid_input(self):
        result = subprocess.run(['python', 'cli.py', '2', 'a'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('error: invalid argument', result.stderr)

    def test_no_input(self):
        result = subprocess.run(['python', 'cli.py'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn('error: the following arguments are required', result.stderr)

if __name__ == '__main__':
    unittest.main()
