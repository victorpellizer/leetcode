class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        """Solução para descobrir se, em uma árvore binária, a soma dos nós até uma folha resulta targetSum"""
        if not root:
            return False

        # como targetSum vai sendo subtraído do valor a cada recursão, se ele for igual ao valor da folha
        # ao chegar nela, então uma rota DFS de fato resulta targetSum
        if not root.right and not root.left and targetSum == root.val:
            return True

        # a chamada recursiva vai subtrair o valor do nó atual e vai percorrer a árvore pela esquerda e direita, até
        # chegar à folha
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
