class Solution:
    def firstUniqChar(self, s: str) -> int:
        """Solução para encontrar o índice do primeiro caractere único dentro de uma string
        """
        d = {} # cria um dict contador de caracteres
        for idx, ch in enumerate(s): # itera sobre a string com acesso ao índice
            if not d.get(ch): # verifica se o caractere não está no dict
                d[ch] = [idx, 1] # se não estiver, salva seu índice com contagem 1
            else:
                d[ch][1] +=1 # se já estiver, incrementa a contagem do índice

        for ch, val in d.items():
            if val[1] == 1: # se o val[1] for 1, significa que é um caractere único
                return val[0] # retorna o índice do primeiro caractere único

        return -1 # resposta padrão caso não existir

