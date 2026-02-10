class Solution:
    def reverseWords(self, s: str) -> str:
        """Solução para desafio de inverter todas palavras em um texto"""
        res = ""  # inicia um texto vazio para resposta
        l, r = 0, 0  # declara os ponteiros da janela

        while r < len(s):
            if s[r] == " ":  # verifica se o caractere é um espaço
                res += s[l : r + 1][
                    ::-1
                ]  # se sim, adiciona a palavra invertida à resposta final
                r += 1  # desloca a janela à direita
                l = r  # começa uma nova janela na nova palavra
            else:
                r += 1  # senão, continua expandindo a janela na palavra

        # como o while encerrou antes de adicionar a última palavra
        res += " "  # adiciona mais um espaço
        res += s[l : r + 2][
            ::-1
        ]  # inverte a última palavra e adiciona à resposta
        return res[
            1:
        ]  # a partir do primeiro, pois adicionamos um espaço em branco ao início da string
