"""Middleware chain decorator for Flask."""
import inspect
from functools import wraps
def middleware_chain(func):
    """Wrap function with middleware chain."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Call each middleware in order."""
        result = None
        for middleware in [lambda x: 'Hello', lambda x: 'World', lambda x: 'Goodbye']:
            if inspect.isfunction(middleware):
                result = middleware(result)
        return func(result) if result is not None else result
    return wrapper
def app(func):
    """Example function to test decorator."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Call example function with middleware chain."""
        return func('Hello World!')
    return wrapper
@app(middleware_chain)
@wrapper
def main():
    print(main())
if __name__ == '__main__':
    main()
