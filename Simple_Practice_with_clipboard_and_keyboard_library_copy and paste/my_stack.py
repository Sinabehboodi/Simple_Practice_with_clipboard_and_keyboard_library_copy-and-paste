from collections import deque


class CStack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
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