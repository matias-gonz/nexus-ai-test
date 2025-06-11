import subprocess
import os
import pytest

# Test cases

def test_copy_file_success(tmp_path):
    # Create a dummy source file
    source_file = tmp_path / "source.txt"
    source_file.write_text("This is the source file.")

    # Define the destination file
    dest_file = tmp_path / "destination.txt"

    # Run the CLI command
    result = subprocess.run(["cargo", "run", "--", str(source_file), str(dest_file)], capture_output=True, text=True)

    # Assert the command was successful
    assert result.returncode == 0
    assert dest_file.read_text() == "This is the source file."


def test_copy_file_overwrite(tmp_path):
    # Create a dummy source file
    source_file = tmp_path / "source.txt"
    source_file.write_text("This is the source file.")

    # Create a destination file with some content
    dest_file = tmp_path / "destination.txt"
    dest_file.write_text("This is the original destination file content.")

    # Run the CLI command
    result = subprocess.run(["cargo", "run", "--", str(source_file), str(dest_file)], capture_output=True, text=True)

    # Assert the command was successful and the destination file was overwritten
    assert result.returncode == 0
    assert dest_file.read_text() == "This is the source file."


def test_copy_file_source_not_found(tmp_path):
    # Define the source and destination files
    source_file = tmp_path / "nonexistent_source.txt"
    dest_file = tmp_path / "destination.txt"

    # Run the CLI command
    result = subprocess.run(["cargo", "run", "--", str(source_file), str(dest_file)], capture_output=True, text=True)

    # Assert the command failed with a non-zero exit code
    assert result.returncode != 0
    assert "No such file or directory" in result.stderr


def test_copy_file_invalid_destination(tmp_path):
    # Create a dummy source file
    source_file = tmp_path / "source.txt"
    source_file.write_text("This is the source file.")

    # Define an invalid destination path
    dest_file = tmp_path / "invalid_dir" / "destination.txt"

    # Run the CLI command
    result = subprocess.run(["cargo", "run", "--", str(source_file), str(dest_file)], capture_output=True, text=True)

    # Assert the command failed with a non-zero exit code
    assert result.returncode != 0
    assert "No such file or directory" in result.stderr
