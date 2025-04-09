class Solution:
    def reverseList(self, head):
        new_list = None # a lista invertida começa como um ponteiro apontando para o nada

        while head: # enquanto head não for nulo
            next_node = head.next # guarda o endereço do nó à frente do head atual
            head.next = new_list # deslinka o head da list antiga, que passa a apontar para a lista invertida
            new_list = head # a lista nova recebe o head da lista antiga
            head = next_node # o head da "lista antiga" passa a ser o next_node

        return new_list