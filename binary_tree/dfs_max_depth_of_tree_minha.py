# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        all_dfs = []

        def dfs(root, steps: int):
            if not root:
                return False
            if not root.right and not root.left:
                all_dfs.append(steps)
            steps += 1
            return dfs(root.left, steps) or dfs(root.right, steps)

        dfs(root, 1)

        return max(all_dfs)
