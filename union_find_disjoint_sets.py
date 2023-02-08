"""Implement union-find disjoint sets."""
import random

def make_set(size):
    """Return a set with the given size."""
    return [i for i in range(size)]

def find(set, x):
    """Find the representative of the set containing x."""
    if set[x] != x:
        set[x] = find(set, set[x])
    return set[x]

def union(set, x, y):
    """Union two sets containing x and y."""
    root_x = find(set, x)
    root_y = find(set, y)
    if root_x != root_y:
        set[root_y] = root_x

if __name__ == "__main__":
    size = 10
    sets = make_set(size)
    for i in range(size):
        print(f"Set {i}: {find(sets, i)}")
    union(sets, 0, 1)
    union(sets, 2, 3)
    print(f"After union: Set 0: {find(sets, 0)}")
    print(f"After union: Set 1: {find(sets, 1)}")"