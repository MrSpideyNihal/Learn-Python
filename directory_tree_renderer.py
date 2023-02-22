"""Render a directory tree as ASCII art."""
import os

def render_directory_tree(directory):
    """Return a string representing the directory tree as ASCII art."""
    result = ''
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = '  ' * (level - 1) if level > 0 else ''
        result += f'{indent}{os.path.basename(root)}' + '
'
    return result

if __name__ == "__main__":
    directory = '/path/to/directory'
    print(render_directory_tree(directory))
