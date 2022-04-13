"""Word frequency counter."""
import collections

def count_words(text):
    """Return a dictionary of word frequencies."""
    return collections.Counter(text.split())

if __name__ == "__main__":
    text = input("Enter text: ")
    print(count_words(text))