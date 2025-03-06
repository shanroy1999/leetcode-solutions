"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Allocating a new memory for every single node - creating new node
        # 2 pass -> 2 loops
        # 1st pass => create copies of input nodes => dont linkt them yet
        #          => map original node to the new node using hashmap
        # 2nd pass => use the hashmap to get to map every old node to new node

        # Hashmap
        # old None node => will have a None copy node
        oldToCopy = { None : None }

        # Iterate through linked list
        curr = head

        # 1st pass of the loop - do not connect the pointer
        # only copy the node to hashmap
        while curr:
            # Cloning linked list node and adding them to hashmap
            copy = Node(curr.val)
            # Map old node to copy node
            oldToCopy[curr] = copy
            # Update current pointer
            curr = curr.next
        
        # 2nd pass of the loop
        curr = head
        while curr:
            # Copy node of the current
            copy = oldToCopy[curr]
            # Set the pointers of the copy node in linked list - next and random
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            # Update current pointer
            curr = curr.next
        
        # return the head of the copy node
        return oldToCopy[head]