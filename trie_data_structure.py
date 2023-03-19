"""Trie data structure implementation."""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

def insert(root, word):
    """Insert a word into the trie."""
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end_of_word = True

def traverse(root, prefix=""): """Traverse the trie and print all words with given prefix."""
    for char in root.children:
        new_prefix = f"{prefix}{char}" if prefix else char
        traverse(root.children[char], new_prefix)
        if root.children[char].is_end_of_word:
            print(new_prefix)

if __name__ == "__main__":
    root = TrieNode()
    words = ['apple', 'banana', 'app', 'ban', 'ap']
    for word in words:
        insert(root, word)
    traverse(root)
