from collections import deque
from typing import Optional


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors: list[Node] = neighbors if neighbors else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        """Solução para clonar um grafo"""
        if not node:
            return node

        q = deque([node])  # cria uma fila pois usarei BFS, e a inicializa com o primeiro nó

        clones = {}  # um hashmap para salvar os nós que já foram clonados
        clones[node.val] = Node(node.val, [])  # inicializa o hashmap com o primeiro nó

        while q:  # enquanto a fila possuir nós
            curr = q.popleft()  # pega o nó mais à esquerda
            curr_clone: Node = clones[curr.val]  # cria um clone do nó atual

            for n in curr.neighbors:  # enquanto o nó atual possuir vizinhos
                if n.val not in clones:  # verifica se o nó não está no hashmap
                    clones[n.val] = Node(n.val, [])  # adiciona o novo nó ao hashmap
                    q.append(n)  # adiciona o novo nó à fila

                curr_clone.neighbors.append(clones[n.val])  # popula o array de vizinhos do nó clone

        return clones[node.val]  # retorna o primeiro nó do grafo clonado
