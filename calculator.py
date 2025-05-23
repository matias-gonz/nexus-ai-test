import sys

def calculate(num1, operator, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "ValueError: Invalid input"

    if operator == '+':
        return str(num1 + num2)
    elif operator == '-':
        return str(num1 - num2)
    else:
        return "Error: Invalid operator"

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <number1> <operator> <number2>")
    else:
        num1, operator, num2 = sys.argv[1], sys.argv[2], sys.argv[3]
        result = calculate(num1, operator, num2)
        print(result)
