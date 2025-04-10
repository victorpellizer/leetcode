# terminar de implementar a árvore para debugar 
class TreeNode:
    pass

class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop()) # remove o índice mais a direita, que é o root da (sub)árvore
        inorder_index = inorder.index(root.val) # detecta onde está o índice do root dentro do (sub)array inorder

        root.right = self.buildTree(inorder[inorder_index+1:], postorder) # folhas da direita são a segunda metade do array inorder
        root.left = self.buildTree(inorder[:inorder_index], postorder) # folhas da esquerda são a primeira metade do array inorder

        return root
