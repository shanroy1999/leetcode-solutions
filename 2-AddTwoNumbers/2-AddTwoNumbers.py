# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        # Handle overflow when sum > 9
        carry = 0

        # Traverse both the linked lists
        # Add numbers digit by digit
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add corresponding digits along with the carry
            total = val1 + val2 + carry

            # L1 = [2, 4, 3] & L2 = [5, 6, 4]
            # val1 = 2 (from l1) and val2 = 5 (from l2)
            # total = 2 + 5 + 0 = 7
            # digit = 7, carry = 0
            # val1 = 4 (from l1) and val2 = 6 (from l2)
            # total = 4 + 6 + 0 = 10
            # digit = 0, carry = 1
            # val1 = 3 (from l1) and val2 = 4 (from l2)
            # total = 3 + 4 + 1 = 8
            # digit = 8, carry = 0
            # result = [7, 0, 8]

            carry = total//10
            digit = total%10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next