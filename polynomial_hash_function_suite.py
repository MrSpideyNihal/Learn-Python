"""Polynomial hash function suite for string matching."""
import random

def polynomial_hash(s, p, m):
    """Return the hash value of the given string using the given polynomial and modulus."""
    result = 0
    for char in s:
        result = (result * p + ord(char)) % m
    return result

def rolling_hash_function(s, p, m):
    """Return a generator that yields the hash values of the given string using the given polynomial and modulus."""
    result = 0
    for char in s:
        yield (result * p + ord(char)) % m
        result = (result * p + ord(char)) % m

if __name__ == "__main__":
    s = 'hello world'
    p = random.randint(1, 1000)
    m = random.randint(100000, 1000000)
    print(polynomial_hash(s, p, m))
    for hash_value in rolling_hash_function(s, p, m):\n        print(hash_value)