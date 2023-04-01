"""Thread-safe task queue."""
import threading

def TaskQueue():
    """Thread-safe task queue class."""
    class Queue:
        def __init__(self):
            self.lock = threading.Lock()
            self.tasks = []

        def put(self, task):
            with self.lock:
                self.tasks.append(task)

        def get(self):
            with self.lock:
                return self.tasks.pop(0) if self.tasks else None

    return Queue()

if __name__ == "__main__":
    queue = TaskQueue()
    for i in range(5):
        queue.put(i)
    print([queue.get() for _ in range(5)])
