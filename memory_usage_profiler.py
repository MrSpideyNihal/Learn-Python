"""Memory usage profiler."""
import gc
class MemoryProfiler:
    """Memory Profiler class."""
    def __init__(self):
        self.memory = 0
    def get_memory(self):
        """Get the current memory usage."""
        return self.memory
    def track(self):
        """Track memory usage and update the profiler."""
        self.memory += gc.get_objects()
    def __str__(self):
        """Return a string representation of the profiler."""
        return f'Memory Usage: {self.memory} bytes'
def main():
    """Example usage of memory profiler."""
    profiler = MemoryProfiler()
    for _ in range(10000):
        profiler.track()
    print(profiler)
if __name__ == '__main__':
    main()
