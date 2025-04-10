class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """Solução ótima para encontrar o único número faltante em um array [0,n], com tamanho n
        Utilizando XOR, o número final é o caractere não encontrado, pois qualquer número A XOR A resulta em zero 
        Então, para a soma final zerar, faltaria fazer XOR com o número que sobrou
        """
        x = 0
        for num in nums:
            x ^= num
        for i in range(len(nums)+1):
            x ^= i

        return x

nums = [3,0,1]
print(Solution().missingNumber(nums))