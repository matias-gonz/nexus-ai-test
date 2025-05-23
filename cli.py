mport argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate the sum of two numbers.")
    parser.add_argument("num1", type=str, help="First number")
    parser.add_argument("num2", type=str, help="Second number")

    args = parser.parse_args()

    try:
        num1 = float(args.num1)
        num2 = float(args.num2)
        sum_ = num1 + num2
        print(f"The sum of {num1} and {num2} is: {sum_}")
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
