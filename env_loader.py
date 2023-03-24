"""Load environment variables from a file."""
import os
import re

def validate(file_path):
    """Validate the given environment variable file."""
    if not os.path.isfile(file_path):
        return False, None
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    pattern = re.compile(r'([A-Z_][a-zA-Z0-9_]*)=([^=]+)')
    variables = {}
    for line in lines:
        match = pattern.match(line)
        if match:
            key, value = match.groups()
            variables[key] = value
    return True, variables

def load(variables):
    """Load the environment variables into the current process."""
    for key, value in variables.items():
        os.environ[key] = value

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python env_loader.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    valid, variables = validate(file_path)
    if valid:
        load(variables)
        print(f"Loaded {len(variables)} environment variables.")
    else:
        print(f"Error: Invalid file {file_path}")
