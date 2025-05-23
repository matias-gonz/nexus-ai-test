import subprocess
import sys


def test_valid_input():
    result = subprocess.run([sys.executable, "simple_sum.py", "5", "10"], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout.strip() == "15"


def test_invalid_input_first_argument():
    result = subprocess.run([sys.executable, "simple_sum.py", "abc", "10"], capture_output=True, text=True)
    assert result.returncode != 0
    assert "error" in result.stderr.lower()


def test_invalid_input_second_argument():
    result = subprocess.run([sys.executable, "simple_sum.py", "5", "abc"], capture_output=True, text=True)
    assert result.returncode != 0
    assert "error" in result.stderr.lower()


def test_no_input():
    result = subprocess.run([sys.executable, "simple_sum.py"], capture_output=True, text=True)
    assert result.returncode != 0
    assert "error" in result.stderr.lower()


def test_one_input():
    result = subprocess.run([sys.executable, "simple_sum.py", "5"], capture_output=True, text=True)
    assert result.returncode != 0
    assert "error" in result.stderr.lower()


# Create a dummy simple_sum.py file for testing
with open("simple_sum.py", "w") as f:
    f.write("""
import argparse

parser = argparse.ArgumentParser(description='Calculate the sum of two integers.')
parser.add_argument('num1', type=int, help='First integer')
parser.add_argument('num2', type=int, help='Second integer')

args = parser.parse_args()

print(args.num1 + args.num2)
""")
