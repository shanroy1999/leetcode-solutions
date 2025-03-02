# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        # Preorder dfs
        def dfs(node):
            # Base case
            if not node:
                res.append("Null")
                return
            # Append the value of the node converted to a string
            res.append(str(node.val))
            # Recursively call dfs on left and right subtrees
            dfs(node.left)
            dfs(node.right)
            # Returns by default
        # Call the dfs on root node
        dfs(root)
        # Return the string of the nodes
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        # Given the data => comma delimited
        # Convert the data into a list of values
        vals = data.split(",")
        # For iteration - global var
        self.i = 0
        def dfs():
            # Base case
            # If pointer points to a Null value => return a None node
            if vals[self.i]=="Null":
                # Increment i
                self.i+=1
                return None
            # If pointer points to a value => create a TreeNode from that value
            node = TreeNode(int(vals[self.i]))
            self.i+=1
            # Recursively call dfs for creating the left and right subtrees
            node.left = dfs()
            node.right = dfs()
            # Return the root node created
            return node
        return dfs()

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans