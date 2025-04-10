class Solution:
    def isSameTree(self, p, q) -> bool:
        """
        Problema: detectar se duas árvores são iguais
        Solução: verifica se o nó é igual, se sim, envia os dois nós esquerdos e os
        dois nós direitos, como sub-árvores, para serem comparados entre si, recursivamente.
        Nisso, ele vai acabar comparando nó por nó, até acabar o call pile.
        """
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False