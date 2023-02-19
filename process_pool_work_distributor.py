"""Process pool work distributor."""
import multiprocessing as mp
def distribute_work(work_items):
    """Distribute work items across the process pool."""
    with mp.Pool(processes=4) as pool:
        results = pool.map(lambda x: x ** 2, range(10))
        print(results)
if __name__ == "__main__":
    distribute_work(range(10))
