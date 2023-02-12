"""Asynchronous producer-consumer pipeline."""
import asyncio
from queue import Queue

def producer(queue):
    """Produce messages and put them in the queue."""
    for i in range(5):
        await queue.put(f"Message {i}")
    print("Producer finished")

async def consumer(queue):
    """Consume messages from the queue and process them."""
    while True:
        message = await queue.get()
        if message == "END":
            break
        print(f"Consumed: {message}")
    print("Consumer finished")

if __name__ == "__main__":
    queue = Queue()
    loop = asyncio.get_event_loop()
    producer_task = loop.create_task(producer(queue))
    consumer_task = loop.create_task(consumer(queue))
    await asyncio.wait([producer_task, consumer_task])"