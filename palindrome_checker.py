"""Check for palindromes."""
import re

def is_palindrome(s):
    """Return True if the input string is a palindrome, False otherwise."""
    return s.lower() == s.lower()[::-1]

if __name__ == "__main__":
    while True:
        user_input = input("Enter a word or 'q' to quit: ")
        if user_input.lower() == 'q':
            break
        elif is_palindrome(user_input):
            print(f"'{user_input}' is a palindrome!"
        else:
            print(f"'{user_input}' is not a palindrome."
