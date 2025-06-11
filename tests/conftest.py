import pytest
import subprocess

@pytest.fixture(scope="session", autouse=True)
def build_project():
    # Build the rust project before running tests
    subprocess.run(["cargo", "build"], check=True, capture_output=True)
