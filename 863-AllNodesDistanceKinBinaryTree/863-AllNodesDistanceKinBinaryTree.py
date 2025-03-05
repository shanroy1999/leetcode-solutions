# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # If k is 0 => 0 distance from target
        if not k:
            return [target.val]
        
        res = []
        parent = {}                     # Track of parents of all nodes => Node : Parent
        visited = set()                 # Mark nodes as visited
        queue = collections.deque()     # do a BFS
        queue.append(root)

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    parent[node.left.val] = node
                    queue.append(node.left)
                
                if node.right:
                    parent[node.right.val] = node
                    queue.append(node.right)
        
        queue.append(target)

        while k>0 and queue:
            for i in range(len(queue)):
                # Pop the root and replace it with the children
                node = queue.popleft()
                visited.add(node.val)
                # Left child
                if node.left and node.left.val not in visited:
                    # Add the node to the parent Hashmap
                    parent[node.left.val] = node
                    # Append the child
                    queue.append(node.left)
                # Right child
                if node.right and node.right.val not in visited:
                    parent[node.right.val] = node
                    queue.append(node.right)
                
                # If the node is already processed
                if node.val in parent and parent[node.val].val not in visited:
                    queue.append(parent[node.val])
            k-=1
        
        while queue:
            res.append(queue.popleft().val)
        
        return res
        



        