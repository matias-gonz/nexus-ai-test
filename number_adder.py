import argparse

def main():
    parser = argparse.ArgumentParser(description='Add two numbers.')
    parser.add_argument('num1', type=int, help='First number')
    parser.add_argument('num2', type=int, help='Second number')

    try:
        args = parser.parse_args()
        sum_result = args.num1 + args.num2
        print(sum_result)
    except ValueError:
        print("Error: Invalid input. Please enter integers only.")
    except SystemExit:
        pass

if __name__ == '__main__':
    main()
