"""Assertion library diff viewer."""
import difflib

def view_diff(filename1, filename2):
    """Return a unified diff of two files."""
    with open(filename1, 'r') as f1:
        contents1 = f1.read()
    with open(filename2, 'r') as f2:
        contents2 = f2.read()
    unified_diff = difflib.unified_diff(contents1.splitlines(), contents2.splitlines())
    return '
'.join(unified_diff)

if __name__ == "__main__":
    print(view_diff('file1.txt', 'file2.txt'))
