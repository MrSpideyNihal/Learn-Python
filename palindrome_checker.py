"""Check if a given string is the same backwards as forwards."""
import re

def is_palindrome(s):
    """Return True if s is a palindrome, False otherwise."""
    s = re.sub(r'\s+', '', s).lower()
    return s == s[::-1]

if __name__ == "__main__":
    print(is_palindrome(input("Enter a string: ")))