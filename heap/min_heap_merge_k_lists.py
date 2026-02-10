import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Solução eficiente para dar merge em N listas encadeadas com o auxílio de uma heap"""
        heap = []  # heap é uma estrutura de dados adequada pois o pop retorna sempre seu menor elemento

        def push_node(heap, node):
            if node:
                heapq.heappush(heap, (node.val, id(node), node))
                # insere o ponteiro da lista encadeada em formato de dupla, pois uma heap é ordenada
                # de acordo com os índices mais à esquerda de uma tupla
                # 1 - node.val é o item em questão
                # 2 - id(node) é o critério de desempate
                # 3 - node é a própria lista encadeada

        for node in lists:
            push_node(heap, node)  # preenche a heap com os heads das listas que serão mergeadas

        dummy = ListNode()  # cria o dummy para apontar para a lista final mergeada
        current = dummy  # ponteiro para manter controle de onde está o tail da lista encadeada

        while heap:  # enquanto a heap possuir dados
            _, _, node = heapq.heappop(heap)  # ao dar pop na heap, sei que estarei pegando o menor nó possível
            current.next = node  # adiciona o nó à fila ordenada
            current = current.next  # current aponta para o vazio, para poder receber o próximo item
            if node.next:  # se ainda existe nó na fila, adiciona à heap, que o colocará na ordem certa
                push_node(heap, node.next)

        return dummy.next
