class Solution:
    def smallestElementRotatedArray(self, arr: list):
        """Solução para encontrar o menor elemento de um array ordenado rotacionado"""
        inicio, fim = 0, len(arr) - 1

        while inicio < fim:
            meio = (inicio + fim) // 2
            if arr[meio] > arr[fim]:
                # Mínimo está na metade da direita
                inicio = meio + 1
            else:
                # Mínimo está na metade da esquerda (inclusive o meio)
                fim = meio
        return arr[inicio]  # retorna o menor elemento do array


array = [4, 5, 6, 7, 1, 2, 3]
print(Solution().smallestElementRotatedArray(array))
