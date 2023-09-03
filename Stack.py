# write a program to implement the stack data structure using array


from array import *

class Stack:
    def __init__(self):
        self.stack = array('i',[])

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def display(self):
        print(self.stack)

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.display()
    s.pop()
    s.display()
    s.pop()
    s.display()

# Output:
# array('i', [1, 2, 3, 4, 5])
# array('i', [1, 2, 3, 4])
# array('i', [1, 2, 3])

# Time Complexity:
# push() - O(1)     
# pop() - O(1)
# display() - O(n)

# Space Complexity:
# push() - O(n) 
# pop() - O(1)
# display() - O(1)

# Write a program to implement the stack data structure using collections.deque

from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def display(self):
        print(self.stack)

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.display()
    s.pop()
    s.display()
    s.pop()
    s.display()

# Output:
# deque([1, 2, 3, 4, 5])
# deque([1, 2, 3, 4])
# deque([1, 2, 3])

# Time Complexity:
# push() - O(1)
# pop() - O(1)
# display() - O(n)

# Space Complexity:
# push() - O(n)
# pop() - O(1)
# display() - O(1)

# Write a program to implement the stack data structure using queue.LifoQueue

from queue import LifoQueue

class Stack:
    def __init__(self):
        self.stack = LifoQueue()

    def push(self, data):
        self.stack.put(data)

    def pop(self):
        if self.stack.empty():
            return None
        return self.stack.get()

    def display(self):
        print(self.stack.queue)

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.display()
    s.pop()
    s.display()
    s.pop()
    s.display()

# Output:
# deque([1, 2, 3, 4, 5])
# deque([1, 2, 3, 4])
# deque([1, 2, 3])

# Time Complexity:
# push() - O(1)
# pop() - O(1)
# display() - O(n)

# Space Complexity:
# push() - O(n)
# pop() - O(1)
# display() - O(1)

# Write a program to implement the stack data structure using queue.Queue

from queue import Queue

class Stack:
    def __init__(self):
        self.stack = Queue()

    def push(self, data):
        self.stack.put(data)

    def pop(self):
        if self.stack.empty():
            return None
        return self.stack.get()

    def display(self):
        print(self.stack.queue)
        

