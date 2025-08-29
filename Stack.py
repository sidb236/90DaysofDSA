class Stack:
    """Simple stack implementation using a Python list."""

    def __init__(self):
        self._items = []

    def push(self, item):
        """Push ``item`` onto the stack."""
        self._items.append(item)

    def pop(self):
        """Pop and return the top item from the stack.

        Returns ``None`` if the stack is empty.
        """
        if not self._items:
            return None
        return self._items.pop()

    def peek(self):
        """Return the top item without removing it or ``None`` if empty."""
        if not self._items:
            return None
        return self._items[-1]

    def is_empty(self):
        """Return ``True`` if the stack is empty."""
        return len(self._items) == 0

    def traverse(self):
        """Return a list representing the current stack order."""
        return list(self._items)


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.traverse())
    print(s.pop())
    print(s.traverse())
