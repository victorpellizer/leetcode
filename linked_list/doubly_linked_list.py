class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node | None = None
        self.prev: Node | None = None

class DoublyLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def add_to_front(self, value):
        new_node = Node(value)
        if not self.head: # se a lista estiver vazia, o novo nó vai ser o tail e o head
            self.head = self.tail = new_node
        else: # senão, adiciona o novo nó na frente, e o novo nó passa a ser o head
            new_node.next = self.head # o novo nó coloca o head como seu próximo, vulgo na segunda posição
            self.head.prev = new_node # como é doubly list, o head antigo precisa apontar para o nó novo
            self.head = new_node # o nó novo passa a ser o head

    def add_to_end(self, value):
        new_node = Node(value)
        if not self.tail: # se a lista estiver vazia, o novo nó vai ser o tail e o head
            self.head = self.tail = new_node
        else: # senão, adiciona o novo nó no fim, e o novo nó passa a ser o tail
            new_node.prev = self.tail # o novo nó coloca o tail como seu anterior, vulgo na penúltima posição
            self.tail.next = new_node # como é doubly list, o tail antigo precisa apontar para o nó novo
            self.tail = new_node # o nó novo passa a ser o tail

    def remove_from_front(self):
        if not self.head: # lista vazia
            return None
        removed_value = self.head.value # salvar o valor antes de excluir
        if self.head == self.tail: # se a lista só tem um valor, head e tail passam a valer nulo
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return removed_value

    def remove_from_end(self):
        if not self.tail: # lista vazia
            return None
        removed_value = self.tail.value # salvar o valor antes de excluir
        if self.head == self.tail: # se a lista só tem um valor, head e tail passam a valer nulo
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return removed_value