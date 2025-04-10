class Stack:
    def __init__(self, max_length=1000):
        self.items = [0] * max_length
        self.max_length = max_length
        self.pointer = 0

    def push(self, item):
        if self.pointer >= self.max_length:
            raise IndexError("Stack overflow")
        self.items[self.pointer] = item
        self.pointer += 1

    def pop(self):
        if self.pointer == 0:
            raise IndexError("Empty stack")
        self.pointer -= 1
        return self.items[self.pointer]

    def peek(self):
        if self.pointer == 0:
            raise IndexError("Empty stack")
        return self.items[self.pointer - 1]

    def size(self):
        return self.pointer
