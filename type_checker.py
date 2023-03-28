"""Type checking decorator."""
import functools

def check_type(func):
    """Return function with runtime type checks."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in [arg for arg in args + list(kwargs.values()) if not isinstance(arg, int)]:
            raise TypeError(f"Argument {arg} must be an integer.")
        return func(*args, **kwargs)
    return wrapper

if __name__ == "__main__":
    @check_type
    def add(a, b):
        """Return sum of two integers."""
        return a + b

print(add(2, 3))
