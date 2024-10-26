from collections import deque 


class CQueue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, value):
        self.container.appendleft(value)

    def dequeue(self):
        if len(self.container):
             return self.container.pop()
        else:
            return ""
        
    def __len__(self):
        return len(self.container)
    
    def __repr__(self):
        return str(self.container)
    
    def is_empty(self):
        return len(self.container) == 0
    
    def atfront(self):
        return self.container[-1]