# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # left and right boundaries of the node
        def isValid(node, left, right):
            if not node:
                return True
            # BST => node values on left < parent node val and node values on right > parent node val
            if not (node.val < right and left < node.val):
                return False
            # Make sure left subtree and right subtree are valid
            # Left subtree => left boundary will be same, right boundary updated => < parent node
            # Right subtree => right boundary will be same, left boundary updated => > parent node
            return isValid(node.left, left, node.val) and isValid(node.right, node.val, right)
        # left boundary => -inf for root node
        # right boundary => +inf for root node
        return isValid(root, float("-inf"), float("inf"))

    # Time Complexity = O(N) => only 2 comparisons for each node of the BST