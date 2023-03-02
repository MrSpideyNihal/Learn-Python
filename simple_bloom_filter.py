"""Simulates a simple bloom filter."""
import bitarray

def SimpleBloomFilter(capacity=100000, false_positive_rate=0.05):
    """Create a simple bloom filter."""
    self.capacity = capacity
    self.size = -(-capacity // 8)
    self.bit_array = bitarray.bitarray(self.size)
    self.hash_functions = hash
    def add(self, item):
        """Add an item to the bloom filter."""
        for seed in self.hash_functions:
            result = (seed * len(item)) % self.capacity
            self.bit_array[result // 8] |= 1 << (result % 8)
    def contains(self, item):
        """Check if an item is present in the bloom filter."""
        for seed in self.hash_functions:
            result = (seed * len(item)) % self.capacity
            if not self.bit_array[result // 8] & (1 << (result % 8)):
                return False
        return True
if __name__ == "__main__":
    bloom_filter = SimpleBloomFilter()
    items = ['apple', 'banana', 'orange', 'grape']
    for item in items:
        bloom_filter.add(item)
    print(bloom_filter.contains('apple'))
