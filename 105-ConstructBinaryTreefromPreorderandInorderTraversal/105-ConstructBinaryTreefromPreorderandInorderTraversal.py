# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # No values
        if not preorder or not inorder:
            return None
        
        # Preorder => (Root, left, right)
        # Inorder => (Left, Root, Right)
        # Create e treeNode - 1st value of preorder always the root node
        root = TreeNode(preorder[0])
        # find the position of root node in inorder
        # Root node will lie in the middle of the list in case of inorder
        # Inorder : Left of root [:mid] => left subtree, right of root [mid+1:] => right subtree
        mid = inorder.index(preorder[0])

        # Build left subtree - all values to the left of root in inorder, 
        #                    - values to the right of root in preorder => till mid
        # Build right subtree - all values to the right of root in inorder
        #                    - values to the right of left subtree in preorder => after mid
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root