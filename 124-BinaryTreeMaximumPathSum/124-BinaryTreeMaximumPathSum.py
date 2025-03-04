# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float("-inf")

        # Recursive helper function
        def maxPathDown(node):
            if not node:
                return 0
            # Handle negative values of nodes
            maxLeft = max(0, maxPathDown(node.left))
            maxRight = max(0, maxPathDown(node.right))
            # Compute the path sum when current node is the bridge
            # Compare that with the best sum found so far
            self.maxi = max(self.maxi, node.val + maxLeft + maxRight)

            return node.val + max(maxLeft, maxRight)
        
        maxPathDown(root)
        return self.maxi