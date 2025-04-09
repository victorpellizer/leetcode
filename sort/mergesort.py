class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def findMiddle(head):
    """Encontra o meio da lista usando um ponteiro rápido e um lento"""
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def mergeTwoLists(l1, l2):
    """Mescla duas listas ordenadas em uma"""
    head = ListNode() # cria um nó vazio
    tail = head # esse nó vazio também tem um tail apontando pra ele

    while l1 and l2:
        if l1.val < l2.val: # se o nó da Lista 1 é menor, ele que entra na fila ordenada
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2 # depois que uma lista chegou ao fim, mescla a outra inteira no fim
    return head.next


def mergesort(head):
    if not head or not head.next: # sem next significa que reduziu a lista a um único nó
        return head

    middle = findMiddle(head) # encontra o meio
    after_middle = middle.next # define o ínicio da lista da direita
    middle.next = None # quebra a conexão entre a lista da direita e a da esquerda

    # quebra as duas novas listas-metade recursivamente, até virarem um único nó
    left = mergesort(head)
    right = mergesort(after_middle)

    sorted_list = mergeTwoLists(left, right)
    return sorted_list


def buildLinkedList(values):
    """Popula uma linkedlist a partir dos dados de um array"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def printLinkedList(head):
    """Função que percorre a lista ordenada, popula um array com os valores da lista e o imprime"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    print(result)


values = [4, 2, 1, 3]
print("Unsorted Linked List:", values)
head = buildLinkedList(values)
sorted_head = mergesort(head)
print("Sorted Linked List:", end=" ")
printLinkedList(sorted_head)