"""Custom collection implementing the iterator protocol."""
from collections.abc import Iterator, Iterable
class CustomCollection(Iterable):
    """Custom collection class."""
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        raise StopIteration
def main():
    """Example usage of custom collection."""
    data = [1, 2, 3, 4, 5]
    collection = CustomCollection(data)
    for item in collection:
        print(item)
if __name__ == '__main__':
    main()
