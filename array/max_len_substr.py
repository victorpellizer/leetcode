class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        """Solução para encontrar o tamanho da maior substring
        que possui no máximo 2 vezes um caractere
        """
        L, R = 0, 0 # os ponteiros que delimitam o window iniciam zerados
        _max = 1
        counter = {} # cria um dict de contadores dos caracteres

        counter[s[0]] = 1 # pré inicia o contador com a primeira letra considerando que já foi encontrada 1x

        while R < len(s) -1:
            R += 1 # desloca o window para a direita
            if counter.get(s[R]): # verifica se o caractere já está no dict contador
                counter[s[R]] += 1 # se estiver, incrementa a contagem
            else:
                counter[s[R]] = 1 # senão, inicia-o com valor 1

            while counter[s[R]] > 2: # comprime o window para a esquerda enquanto o caractere à direita existir mais de 2x
                counter[s[L]] -= 1 # diminui a contagem do caractere à esquerda, pois foi removido do window
                L += 1 # desloca o window para a esquerda
            _max = max(_max, R-L+1) # compara se o window (vulgo substring) atual é a maior já encontrada

        return _max
