import os
class stack:
    def __init__(self):
        self.items = [];

    def isEmpty(self):
        return len(self.items) == 0;
    
    def push(self, item):
        self.items.append(item);

    def pop(self):
        return self.items.pop();

    def peek(self):
        return self.items[len(self.items)-1];