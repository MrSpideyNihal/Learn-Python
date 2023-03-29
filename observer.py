"""Event bus for observer pattern."""
import threading
from queue import Queue
class EventBus:
    """Event bus for observer pattern."""
    def __init__(self):
        self.queue = Queue()
        self.lock = threading.Lock()

    def post(self, event):
        """Post an event to the queue."""
        with self.lock:
            self.queue.put(event)

    def listen(self, listener):
        """Listen for events and call listener."""
        while True:
            event = self.queue.get()
            with self.lock:
                listener(event)
            self.queue.task_done()

if __name__ == "__main__":
    def print_event(event):
        print(f"Event: {event}")

bus = EventBus()
bus.listen(print_event)
bus.post("Hello, World!")
