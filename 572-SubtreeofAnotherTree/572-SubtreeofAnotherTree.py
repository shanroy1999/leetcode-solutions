# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Traverse the root tree using DFS
        # for each node in root => check if subtree rooted at that node is identical to subroot
        # Compare tree structure and node values recursively for identical trees

        # Empty tree always a subtree
        if subRoot == None:
            return True
        # Empty tree cannot have a subtree
        if root == None:
            return False
        # Current node is root tree matches the structure and value of subRoot tree
        if self.same(root, subRoot):
            return True

        # Recursive call isSubtree on left and right subtrees of root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def same(self, main, sub):
        # if both main and sub trees are None => empty trees are same -> return True
        if main==None and sub==None:
            return True
        
        # one tree is empty and other is non-empty => return False
        if main==None or sub==None:
            return False
        
        # If values of current nodes of main and sub tree are equal
        if main and sub and main.val == sub.val:
            # Recursively call same on left subtrees of main and sub
            # Recursively call same on right subtrees of main and sub
            # If both recursive calls -> return True => subtrees rooted at main and sub are same
            return self.same(main.right, sub.right) and self.same(main.left, sub.left)
        
        return False

    # Time Complexity => O(M x N) -> M = number of nodes in root, N = number of nodes in SubRoot
    # Space Complexity => O(M) -> recursion