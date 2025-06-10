import subprocess
import os
import unittest

class TestFileCopy(unittest.TestCase):

    def setUp(self):
        # Create a dummy file for testing
        self.source_file = "test_source.txt"
        with open(self.source_file, "w") as f:
            f.write("This is a test file.")
        self.destination_file = "test_destination.txt"

    def tearDown(self):
        # Remove the test files
        if os.path.exists(self.source_file):
            os.remove(self.source_file)
        if os.path.exists(self.destination_file):
            os.remove(self.destination_file)

    def test_file_copy_success(self):
        # Call the file_copier.py script
        result = subprocess.run(["python", "file_copier.py", self.source_file, self.destination_file],
                               capture_output=True, text=True)

        # Assert that the script ran successfully
        self.assertEqual(result.returncode, 0)

        # Assert that the destination file exists
        self.assertTrue(os.path.exists(self.destination_file))

        # Assert that the destination file has the same content as the source file
        with open(self.source_file, "r") as source:
            with open(self.destination_file, "r") as destination:
                self.assertEqual(source.read(), destination.read())

    def test_file_copy_source_not_found(self):
        # Call the file_copier.py script with a non-existent source file
        result = subprocess.run(["python", "file_copier.py", "non_existent_file.txt", self.destination_file],
                               capture_output=True, text=True)

        # Assert that the script returned an error code
        self.assertNotEqual(result.returncode, 0)

        # Assert that the destination file does not exist
        self.assertFalse(os.path.exists(self.destination_file))

if __name__ == '__main__':
    unittest.main()
