class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Solução para encontrar a maior substring que não repete nenhum caractere
        """
        char_set = set() # como não pode haver duplicidade, set é uma boa escolha para a janela
        esq = 0 # ponteiro esquerdo no início da string
        res = 0 # zero pois a string pode ser vazia

        for i, dir in enumerate(s): # itera sobre a string em O(n)
            # se um caractere existe no set, ele está duplicado. Então, é necessário
            # encolher a window até ser removido do set o caractere igual ao novo
            while s[dir] in char_set:
                char_set.remove(s[esq]) # remove um caractere à esquerda
                esq += 1 # encolhe a window
            char_set.add(s[dir]) # adiciona um caractere à direita
            res = max(res, len(char_set)) # compara se o tamanho atual é maior que o máximo encontrado
        return res # retorna o maior length encontrado
