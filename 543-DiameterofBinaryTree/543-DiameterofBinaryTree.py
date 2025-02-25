# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        # Helper function to calculate depth of binary tree using recursion
        def dfs(node):
            # if root node is None => empty node -> depth = 0
            if not node:
                return 0
            # Recursive call to left child and right child
            left = dfs(node.left)           # depth of left subtree
            right = dfs(node.right)         # depth of right subtree
            # sum of left depth and right depth
            self.max_diameter = max(self.max_diameter, left + right)
            return max(left, right) + 1
        
        dfs(root)
        return self.max_diameter
