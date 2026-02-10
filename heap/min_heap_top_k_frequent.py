from heapq import heappop, heappush
from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Solução para encontrar os k elementos mais frequentes em um array"""
        heap = []
        # heap é uma abordagem interessante, pois, combinado com Counter, é possível gerar um array ordenado dos índices com base na sua frequência
        counter = Counter(nums)  # retorna um dict com a quantidade de cada um dos índices do array

        for num, count in counter.items():
            # insere os índices encontrados, fazendo a heap os ordenar com base na qtd de cada um
            heappush(heap, (count, num))
            if len(heap) > k:
                # remove os itens menos frequentes, ou seja, os mais à esquerda, até que a heap tenha tamanho k
                heappop(heap)

        return [num for _, num in heap]  # gera um array com os índices que restaram na heap


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution().topKFrequent(nums, k))
