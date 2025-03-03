# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Iterative solution using a stack
        # number of elements visited from tree
        # if n == k => return value
        n = 0
        stack = []

        # node we are at currently
        curr = root

        # while current node is not null or the stack is not empty
        while curr or stack:
            # Keep going left before visiting current node
            while curr:
                # Go back to current node after left subtree processed
                # Store the current node in the stack
                stack.append(curr)
                curr = curr.left
            
            # Loop ends => Now curr = null => went too far
            # Pop the most recently added element from the stack 
            # we are processing the element
            curr = stack.pop()
            n+=1
            if n==k:
                return curr.val
            # Update current to right subtree if left subtree processed
            curr = curr.right


