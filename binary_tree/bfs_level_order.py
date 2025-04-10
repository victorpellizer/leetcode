import collections


class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        """
        Problema: retorne um array de arrays de nós para cada nível de uma árvore
        Solução escolhida: BFS é mais adequada pois faz a busca linha por linha, retornando os nós já na ordem que o exercício pede
        """
        
        res = []
        q = collections.deque() # fila para implementar a BFS
        q.append(root) # insere o root no BFS

        while q:
            level = [] # os nós de um nível são delimitados dentro de um array interno
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    
                    if node.right:
                        q.append(node.right)

            # quando todos os nós de um nível saem da fila, a fila terá todos (e apenas) nós do novo nível
            if level:
                res.append(level)

        return res


