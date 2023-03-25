"""Tokenize input string."""
import re

def tokenize(input_string):
    """Return list of tokens from input string."""
    return [token.group() for token in re.finditer(r'\b\w+\b', input_string.lower())]

if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print(tokenize(text))
