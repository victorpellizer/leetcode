class Solution:
    def hammingWeight(self, n: int) -> int:
        """Solução ótima para encontrar o número de bits 1 em um número"""
        bits = 0
        while n:
            if n & 1: # verifica se o bit é 1
                bits+=1 # se sim, incrementa o contador
            n>>=1 # right-shift de 1 bit até zerar
        return bits
