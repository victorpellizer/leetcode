import heapq


class KthLargest:
    """Solução para o problema de uma universidade que pode aceitar até k alunos,
    cuja nota de corte para entrada dos alunos pode se alterar sempre que é adicionado
    um novo aluno.
    O input é um array de notas/aluno"""

    def __init__(self, k: int, nums: list[int]):
        self.min_heap = nums
        self.k = k
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]
