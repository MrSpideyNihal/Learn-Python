"""Find duplicate files in a directory."""
import os

def find_duplicates(directory):
    """Scan a directory and find duplicate files."""
    file_dict = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            if path in file_dict:
                file_dict[path].append(file)
            else:
                file_dict[path] = [file]

    duplicates = [(k, v) for k, v in file_dict.items() if len(v) > 1]
    return duplicates

if __name__ == "__main__":
    directory = '/path/to/directory'
    duplicates = find_duplicates(directory)
    for duplicate in duplicates:
        print(f"Duplicate files: {duplicate[0]} ({', '.join(duplicate[1])})")