"""Shared memory counter for multiprocess applications."""
import multiprocessing as mp

def get_shared_memory_usage():
    """Return total shared memory size in bytes."""
    return sum([p.memory_info().rss for p in mp.current_process().children]) + mp.get_start_method().memory_info().rss

if __name__ == "__main__":
    print(get_shared_memory_usage())
