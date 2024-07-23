from collections import deque

class Stack:
    def __init__(self):
        self.elements = deque([])

    def push(self, data):
        self.elements.appendleft(data)

    def pop(self):
        if not self.elements:
            raise IndexError("Empty Stack")
        return self.elements.popleft()

# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)

# print(s.elements)

# s.pop()
# s.pop()

# print(s.elements)

# REVERSING A STRING USING STACK

def Reverse_String(string):
    """Get a string and return its reversed version"""
    s = Stack()
    new_string = ""

    for char in string:
        s.push(char)

    while s.elements:
        new_string += s.pop()
        
    return new_string

r = Reverse_String("We will conquere COVI-19")

print(r)