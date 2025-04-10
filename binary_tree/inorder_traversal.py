class Solution:
    def inorderTraversal(self, root) -> list[int]:
        """Implementação de uma inorder traversal numa binary tree em apenas uma linha usando recursão"""
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []

        return inorder(root)
