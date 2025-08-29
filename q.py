from collections import deque


class Queue:
    """Queue implementation using ``collections.deque``."""

    def __init__(self):
        self._items = deque()

    def add(self, item):
        """Add ``item`` to the end of the queue."""
        self._items.append(item)

    def remove(self):
        """Remove and return the item from the front of the queue.

        Returns ``None`` if the queue is empty.
        """
        if not self._items:
            return None
        return self._items.popleft()

    def traverse(self):
        """Return a list representing the current queue order."""
        return list(self._items)

    def is_empty(self):
        """Return ``True`` if the queue is empty."""
        return len(self._items) == 0


if __name__ == "__main__":
    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    print(q.traverse())
    print(q.remove())
    print(q.traverse())
