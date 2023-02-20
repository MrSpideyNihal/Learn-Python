"""Resolve dependencies between test fixtures."""
import heapq

def resolve_dependencies(dependencies):
    """Return a dictionary where keys are fixture names and values are lists of dependent fixtures."""
    result = {}
    for dependency in dependencies:
        for key, value in dependency.items():
            if key not in result:
                result[key] = []
            result[key].append(value)

    return result

if __name__ == "__main__":
    dependencies = [{'A': ['B', 'C']}, {'B': ['D'], 'C': ['E']}]
    print(resolve_dependencies(dependencies))
