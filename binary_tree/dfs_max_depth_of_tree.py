class Solution:
    def maxDepth(self, root) -> int:
        if not root:  # If the current node (root) is None:
            return 0  # Return 0 because an empty subtree has a depth of 0.
        # The function makes recursive calls to compute:
        # The depth of the left subtree (self.maxDepth(root.left)).
        # The depth of the right subtree (self.maxDepth(root.right)).
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
