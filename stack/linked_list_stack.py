class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.top is None:
            raise IndexError("Empty stack")
        popped_node = self.top
        self.top = popped_node.next
        self._size -= 1
        return popped_node.value

    def peek(self):
        if self.top is None:
            raise IndexError("Empty stack")
        return self.top.value

    def size(self):
        return self._size
