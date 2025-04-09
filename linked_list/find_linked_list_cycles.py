class Solution:
    def hasCycle(self, head) -> bool:
        """Solução com dois ponteiros, um rápido e um lento
        Se existe um ciclo, significa que um next eventualmente voltará a um nó que já foi visitado pelo fast
        E em algum momento o slow vai alcançar este fast, pois ele ficará voltando ao mesmo nó
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

