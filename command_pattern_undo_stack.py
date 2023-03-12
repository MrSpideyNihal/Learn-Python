"""Command pattern for undo/redo functionality."""
import collections

def CommandStack():
    """Manage a list of commands."""
    class Stack:
        def __init__(self):
            self.stack = []
        def push(self, cmd):
            self.stack.append(cmd)
        def pop(self):
            return self.stack.pop()
        def clear(self):
            self.stack.clear()

    return Stack()

if __name__ == "__main__":
    stack = CommandStack()
    for _ in range(10):
        stack.push(lambda x: print(f"Command {x} executed."))
    while stack.stack:
        stack.pop()()