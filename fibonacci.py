"""Fibonacci sequence generator."""
import time

def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(3, n+1):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    start = time.time()
    print(fibonacci(10))
    end = time.time()
    print(f"Time: {end - start:.2f} seconds")