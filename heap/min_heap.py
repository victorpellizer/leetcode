class MinHeap:
    def __init__(self):
        self.heap: list[int] = []

    def parent(self, index: int) -> int:
        return (index - 1) // 2

    def left_child(self, index: int) -> int:
        return 2 * index + 1

    def right_child(self, index: int) -> int:
        return 2 * index + 2

    def heapify_up(self, index: int) -> None:
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = (
                self.heap[index],
                self.heap[self.parent(index)],
            )
            index = self.parent(index)

    def heapify_down(self, index: int) -> None:
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )
            self.heapify_down(smallest)

    def insert(self, value: int) -> None:
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def extract_min(self) -> int:
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return root

    def peek(self) -> int:
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def size(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        return len(self.heap) == 0
