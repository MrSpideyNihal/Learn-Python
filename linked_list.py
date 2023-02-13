"""A basic linked list class."""
import sys
from typing import Any
class Node:
    """A node in the linked list."""
    def __init__(self, value: Any):
        self.value = value
        self.next = None
    def __str__(self) -> str:
        return f'Node({self.value})'

class LinkedList:
    """A basic linked list class."""
    def __init__(self):
        self.head = None
    def append(self, value: Any):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
    def __str__(self) -> str:
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current))
            current = current.next
        return ' -> '.join(nodes)

if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print(ll)
