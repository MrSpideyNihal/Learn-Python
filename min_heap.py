"""Min-heap implementation for priority queue."""
import heapq

def PriorityQueue(maxsize=0):
    """Priority queue with a minimum heap."""
    self._queue = []
    self._maxsize = maxsize

    def put(self, item, priority):
        """Put an item into the priority queue."""
        heapq.heappush(self._queue, (-priority, item))
        if len(self._queue) > self._maxsize:
            heapq.heappop(self._queue)

    def get(self):
        """Get the next item from the priority queue."""
        return heapq.heappop(self._queue)[1]

if __name__ == "__main__":
    pq = PriorityQueue(3)
    for i in range(5):
        pq.put(i, i * 2)
    print([pq.get() for _ in range(5)])
