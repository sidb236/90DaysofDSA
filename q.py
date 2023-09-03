
#write a program to implement the queue data structure using list

class Queue:
    def __init__(self):
        self.queue = []

    def add(self, data):
        self.queue.append(data)

    def remove(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

if __name__ == '__main__':
    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    q.add(4)
    q.add(5)
    q.display()
    q.remove()
    q.display()
    q.remove()
    q.display()

# Output:
# [1, 2, 3, 4, 5]
# [2, 3, 4, 5]
# [3, 4, 5]

#write a program to implement the queue data structure using collections.deque

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def add(self, data):
        self.queue.append(data)

    def remove(self):
        if len(self.queue) < 1:
            return None
        return self.queue.popleft()

    def display(self):
        print(self.queue)

if __name__ == '__main__':
    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    q.add(4)
    q.add(5)
    q.display()
    q.remove()
    q.display()
    q.remove()
    q.display()

# Output:
# deque([1, 2, 3, 4, 5])
# deque([2, 3, 4, 5])
# deque([3, 4, 5])

#write a program to implement the queue data structure using queue.Queue

from queue import Queue

q = Queue(maxsize=3)
print(q.qsize())
q.put('a')
q.put('b')
q.put('c')
print("Full: ", q.full())
print("Size: ", q.qsize())
print(q.get())
print(q.get())
print(q.get())
print("Empty: ", q.empty())


#write a program to implement the queue data structure using queue.LifoQueue

from queue import LifoQueue

q = LifoQueue(maxsize=3)
print(q.qsize())
q.put('a')
q.put('b')
q.put('c')
print("Full: ", q.full())
print("Size: ", q.qsize())
print(q.get())
print(q.get())
print(q.get())
print("Empty: ", q.empty())

#write a program to implement the queue data structure using queue.PriorityQueue

from queue import PriorityQueue

q = PriorityQueue()
q.put((1, 'Priority 1'))
q.put((3, 'Priority 3'))
q.put((2, 'Priority 2'))

while not q.empty():
    print(q.get())

# Output:
# (1, 'Priority 1')
# (2, 'Priority 2')
# (3, 'Priority 3')

