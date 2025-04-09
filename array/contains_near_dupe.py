class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """Solução para detectar se um subarray de tamanho k possui números repetidos 
        """
        window = set() # cria um set para representar o sliding window
        L = 0 # inicia o ponteiro L no zero

        if len(nums) < 1 or k == 0: # edge cases para array vazio ou intervalo nulo
            return False

        for R in range(len(nums)): # desloca a window para a direita no array
            if nums[R] in window: # verifica se o numero já existe no set
                return True # se sim, é porque está repetido, então interrompe a execução

            if R - L + 1 > k: # verifica se o window é maior que K
                window.remove(nums[L]) # remove o elemento da esquerda, pois vai sair do window
                L += 1 # move o ponteiro da esquerda

            window.add(nums[R]) # adiciona o elemento novo da direita ao set

        return False
