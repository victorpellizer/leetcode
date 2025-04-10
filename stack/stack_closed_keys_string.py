class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}  # o mapping possui apenas "fechamentos"

        for ch in s:  # itera pela strng
            if ch in mapping:  # se o elemento não estiver no mapping, ele não é interessante
                if stack and stack[-1] == mapping[ch]:
                    # se o último elemento da stack é uma abertura para o fechamento atual. Ex: ] para [
                    stack.pop()  # remove da stack e prossegue
                else:
                    # se não existir uma stack e tentar fechar, ou se tentar fechar com o errado, já deu erro
                    return False
            else:  # vai preenchendo a stack com as aberturas
                stack.append(ch)

        return len(stack) == 0  # se a stack estiver vazia no final, é porque a string é válida
