# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the middle of the list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next                # Shift slow pointer by 1
            fast = fast.next.next           # Shift fast pointer by 2

        second = slow.next                  # Beginning of the second half of the list
        prev = slow.next = None              

        # Reverse the second half of the list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Merge the 1st half and the reversed second half
        second = prev
        first = head

        while second:
            temp1, temp2 = first.next, second.next
            first.next, second.next = second, temp1
            first, second = temp1, temp2