# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Approach 1 : Recursive DFS
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # Approach 2 : Recursive BFS - using queue
        # if not root:
        #     return 0
        # # Use a queue initialized with the root node
        # q = collections.deque([root])
        # level = 0
        # while q:
        #     for i in range(len(q)):
        #         # Remove the node and replace with its children
        #         # Increment the level
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level+=1
        # # Once queue empty => all nodes traversed => return the level
        # return level

        # Approach 3 : Iterative DFS - using stack
        res = 0
        if not root:
            return 0
        stack = [[root, 1]]     # Initialize the stack with the root node and depth
        while stack:
            # pop the stack whenever a level completed
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1]) 
                stack.append([node.right, depth+1])
        return res