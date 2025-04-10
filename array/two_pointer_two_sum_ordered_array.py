class Solution:
    def twoSumOrderedArray(self, nums: list[int], target: int) -> list[int]:
        """Solução para obter dois índices que somam target em um array ordenado"""
        L = 0  # L sempre começa no início do array
        R = len(nums) - 1  # por estar ordenado, o ponteiro R começa no fim do array

        while R > L:  # inteira enquanto os ponteiros estiverem separados
            total = nums[L] + nums[R]
            if total == target:
                return [L, R]  # se encontrou a soma de target, acabou o exercício
            elif total > target:  # se a soma for maior que o target
                R -= 1  # deslocamos o ponteiro da direita para a esquerda para diminuir a soma
            else:  # se for menor
                L += 1  # deslocamos o ponteiro da esquerda para a direita para aumentar a soma

        return [-1, -1]  # resposta convencionada caso target não tenha sido encontrado
