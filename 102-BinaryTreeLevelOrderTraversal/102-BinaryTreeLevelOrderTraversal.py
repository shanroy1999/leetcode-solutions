# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS using a queue
        res = []
        queue = collections.deque()
        # Start from the 1st level of the tree => root node
        queue.append(root)
        # BFS while queue is non empty
        while queue:
            # get number of values in the queue
            lenQueue = len(queue)
            # Sublist in which we will add nodes
            level = []
            # Iterate through the length of queue
            for ele in range(len(queue)):
                # FIFO
                node = queue.popleft()
                # If the queue is not empty
                if node:
                    # Add node to the sublist for the particular level
                    level.append(node.val)
                    # Add the children of the node simultaneously to the queue if any
                    queue.append(node.left)
                    queue.append(node.right)
            # Once the level completed => queue is empty
            # Add the sublist of the level into the result
            # Make sure level is non-empty => not add null nodes to the list
            if level:
                res.append(level)
        # No nodes left in the queue => went through every single level
        return res

        # Time complexity = O(N) => visiting each node only once
        # Space complexity = O(N) => queue can have upto N/2 elements -> biggest level of BST