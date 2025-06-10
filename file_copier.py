import argparse
import shutil
import os


def main():
    parser = argparse.ArgumentParser(description="Copy a file from source to destination.")
    parser.add_argument("source", help="Source file path")
    parser.add_argument("destination", help="Destination file path")
    args = parser.parse_args()

    source_path = args.source
    destination_path = args.destination

    try:
        # Check if the source file exists
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"Source file '{source_path}' not found.")

        # Copy the file
        shutil.copy2(source_path, destination_path)
        print(f"File copied from '{source_path}' to '{destination_path}' successfully.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except OSError as e:
        print(f"Error: Invalid destination path: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
