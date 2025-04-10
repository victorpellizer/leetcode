class Solution:
    def numberOfSteps(self, num: int) -> int:
        """Solução ótima para encontrar o número de passos (divisão + subtração) para um número
        chegar a zero"""
        steps = 0
        while num > 0:
            if num & 1: # & 1 verifica se o último bit é 1, ou seja, ímpar
                num-=1
            else:
                num>>=1 # >>=1 significa right-shift de 1 bit para a direita, ou seja, divide por 2
            steps+=1
        return steps
