# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if the subroot is null => empty tree is subtree of every tree => return true
        if not subRoot:
            return True
        # if the parent itself is null => empty tree cannot have any subtree => return False
        if not root:
            return False
        # if the two trees are exactly the same => return True
        if self.isSameTree(root, subRoot):
            return True
        # see if left or right subtree of the parent tree matches the corresponding subRoot
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    # Check if the two complete trees are exactly the same
    def isSameTree(self, s, t):
        # If both trees are null => same -> return True
        if not s and not t:
            return True
        # If the trees are not null and the values are the same => compare left and right nodes respectively
        if s and t and s.val == t.val:
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
        return False