# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Brute Force Approach
        # Traverse all the linked lists and collect all values into a single list
        # Sort the list
        # Create new linked list from sorted list
        values = []
        for l in lists:
            while l:
                values.append(l.val)
                l = l.next
        
        values.sort()

        dummy = ListNode()
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next