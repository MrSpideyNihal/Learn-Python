"""Breadth-First Search (BFS) traversal."""
import collections

def bfs(graph, start):
    """Return BFS traversal starting from node 'start' in the 'graph'."""
    visited = set()
    queue = collections.deque([start])
    traversal_order = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return traversal_order

if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': ['B'], 'E': ['F'], 'F': []}
    print(bfs(graph, 'A'))