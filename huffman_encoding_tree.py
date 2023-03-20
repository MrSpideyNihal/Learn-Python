"""Huffman encoding tree for compression."""
import heapq
class Node:
    """Node class for Huffman tree."""
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
def build_tree(frequencies):
    """Build the Huffman encoding tree from frequencies."""
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    return heap[0]
def huffman_encoding(tree):
    """Huffman encode a string using the tree."""
    codes = {}
    def traverse(node, prefix):
        if node:
            if node.char:
                codes[node.char] = prefix
            traverse(node.left, prefix + '0')
            traverse(node.right, prefix + '1')
    traverse(tree, '')
    return codes
if __name__ == '__main__':
    frequencies = {'A': 10, 'B': 5, 'C': 5}
    tree = build_tree(frequencies)
    encoding = huffman_encoding(tree)
    print(encoding)
