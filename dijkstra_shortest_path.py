"""Simulates a simple graph and uses Dijkstra's algorithm to find the shortest path."""
import heapq

def dijkstra(graph, start, end):
    """Return the shortest path from start to end using Dijkstra's algorithm."""
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances[end]
if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'D': 2},
        'C': {},
        'D': {}
    }
    print(dijkstra(graph, 'A', 'D'))
