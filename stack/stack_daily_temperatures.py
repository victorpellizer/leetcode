class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """Solução ótima para encontrar quantos dias faltam para o próximo dia mais quente do
        que hoje.
        Input é um array de temperaturas de dias seguidos, o retorno deve ser um array
        contendo N dias que faltam para a temperatura subir.
        Exemplo:
        Input: temperatures = [73,74,75,71,69,72,76,73]
        Output: [1,1,4,2,1,1,0,0]

        """
        results = [0] * len(temperatures)  # inicializa o array de resposta de acordo com o tam do input

        stack = []  # inicializa a pilha na qual serão armazenados os índices cuja >temperatura ainda não foi superada<

        for i, temp in enumerate(temperatures):  # iterar sobre as temperaturas, com acesso aos índices
            while stack and temperatures[stack[-1]] < temp:
                # enquanto a stack possuir dados e a temp do último índice da stack for menor que a encontrada
                # > a temperatura a ser comparada com a atual do for atualiza sempre que um índice é removido da stack
                index = stack.pop()  # restaura da pilha o índice antigo que foi superado
                results[index] = i - index
                # salva no array final o num de iterações para encontrar uma temperatura maior

            stack.append(i)  # vai adicionar um índice à stack ao fim de toda iteração

        return results


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(temperatures))
