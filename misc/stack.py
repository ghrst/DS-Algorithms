# Problem: Implement a stack data structure


class Stack():
    def __init__(self):
        self.items = []


    def is_empty(self):
        return len(self.items) == 0


    def top(self):
        if self.is_empty():
            return None
        else:
            return self.items[len(self.items) - 1]


    def push(self, item):
        self.items.append(item)


    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop()