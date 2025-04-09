class Solution:
    def middleNode(self, head):
        """Como o objetivo é encontrar a metade da lista encadeada,
        esse algoritmo usa um ponteiro head com velocidade 1 e o ponteiro ahead com velocidade 2
        quando o ahead chegar ao fim da lista, significa que o head chegou ao meio dela.
        Basta retornar o head que ele é o meio da lista
        """
        ahead = head

        while ahead and ahead.next:
            ahead = ahead.next.next
            head = head.next

        return head