"""LRU Cache Implementation."""
from collections import OrderedDict

def lru_cache(max_size):
    """Return an ordered dictionary that implements LRU cache."""
    cache = OrderedDict()
    def decorator(func):
        """Memoize the function."""
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            if key in cache:
                result = cache.pop(key)
                return result
            else:
                result = func(*args, **kwargs)
                cache[key] = result
                if len(cache) > max_size:
                    cache.popitem(last=False)
                return result
        return wrapper
    return decorator

if __name__ == "__main__":
    @lru_cache(3)
    def fib(n):
        """Return the nth Fibonacci number."""
        if n <= 1:
            return n
        return fib(n-1) + fib(n-2)
    print(fib(5))
