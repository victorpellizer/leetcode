class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hmap = {} # cria um hashmap
        n = len(nums)
        for i in range(n): # itera pelo array uma vez
            comp = target - nums[i] # salva o valor necessário (complemento) para nums[i] chegar ao target
            if comp in hmap: # verifica se o complemento já existe
                return [hmap[comp],i] # se já existe, então encontramos os dois índices que somam target: o do complemento, e o atual
            hmap[nums[i]] = i # guarda o valor como índice, e o índice do array como valor no hashmap
        return []
