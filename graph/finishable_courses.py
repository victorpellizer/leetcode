class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """Solução para descobrir se um conjunto de cursos é possível de ser concluído.
        Para ser possível de ser concluído, precisa existir um caminho a se percorrer, sem
        haver casos de um curso A dependender de outro curso B ao mesmo ao mesmo tempo que
        B depende de A."""

        # primeiramente, converte o array de entrada em um dict de grafo, que é mais legível
        # e prático de se trabalhar
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)

        state = [0] * numCourses # cria um vetor de zeros, com cada índice representando um dos cursos existentes
        # 0 = curso não visitado
        # 1 = curso em visita
        # 2 = curso visitado

        def has_cycle(v):
            if state[v] == 1:
                return True
            if state[v] == 2:
                return False

            state[v] = 1
            for neighbor in graph[v]:
                if has_cycle(neighbor):
                    return True
            state[v] = 2
            return False

        for i in range(numCourses):
            if has_cycle(i):
                return False

        return True


numCourses = 2
prerequisites = [[1, 0]]
Solution().canFinish(numCourses, prerequisites)
