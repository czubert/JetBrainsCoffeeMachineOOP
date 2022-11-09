class Stack:

    def __init__(self):
        self.container = []

    def push(self, el):
        self.container.append(el)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return not bool(self.container)


