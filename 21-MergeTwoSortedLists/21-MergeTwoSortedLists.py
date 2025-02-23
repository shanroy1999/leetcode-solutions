# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Brute force approach
        # values = []
        # while list1:
        #     values.append(list1.val)
        #     list1 = list1.next
        # while list2:
        #     values.append(list2.val)
        #     list2 = list2.next
        
        # values.sort()
        # dummy = ListNode()
        # current = dummy
        # for val in values:
        #     current.next = ListNode(val)
        #     current = current.next
        # return dummy.next

        # Time complexity = O((M+N)log(M+N))
        # Space complexity = O(M+N) -> sorting and creating new list

        # Optimized Approach
        dummy = ListNode()
        current = dummy

        # Traverse both lists
        while list1 and list2:
            # Compare values at current positions and append smaller values to merged list
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # if one list exhausted => append remaining nodes from other list
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next