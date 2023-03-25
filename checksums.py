"""Calculate and compare the checksums of given files."""
import hashlib
import os

def calculate_checksum(file_path):
    """Calculate the checksum for the given file."""
    with open(file_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def compare_checksums(file1, file2):
    """Compare the checksums of two files."""
    checksum1 = calculate_checksum(file1)
    checksum2 = calculate_checksum(file2)
    if checksum1 == checksum2:
        return f"Checksums match: {checksum1}"
    else:
        return f"Checksums do not match: {checksum1} != {checksum2}"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python checksums.py <file1> <file2>")
        sys.exit(1)
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    try:
        result = compare_checksums(file1, file2)
        print(result)
    except FileNotFoundError as e:
        print(f"Error: File not found - {e.filename}")
