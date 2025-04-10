class Solution:
    def countBits(self, n: int) -> list[int]:
        """Solução ótima para encontrar o número de bits 1 em um array de números sequenciais de 0 até n"""
        ans = []
        for i in range(n+1):
            bits = 0
            num = i
            while num:
                if num & 1: # verifica se o bit é 1
                    bits+=1 # se sim, incrementa o contador
                num>>=1 # right-shift de 1 bit até zerar
            ans.append(bits)
        return ans
