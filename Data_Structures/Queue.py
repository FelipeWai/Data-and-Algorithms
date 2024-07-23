from collections import deque

class Queue():
    def __init__(self):
        self.elements = deque([])

    def enqueue(self, data):
        self.elements.append(data)

    def dequeue(self):
        self.elements.popleft()

    def __str__(self):
        return str(list(self.elements))
    
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q)

q.dequeue()

print(q)