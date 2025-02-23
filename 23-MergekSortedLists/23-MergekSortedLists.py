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
        # values = []
        # for l in lists:
        #     while l:
        #         values.append(l.val)
        #         l = l.next
        
        # values.sort()

        # dummy = ListNode()
        # current = dummy
        # for val in values:
        #     current.next = ListNode(val)
        #     current = current.next
        
        # return dummy.next

        # Time complexity = O(N log N) => N is total number of nodes
        # Space complexity = O(N) => storing the values and creating new linked list

        # Optimized approach
        # Push first node of each linked list in a min-heap
        # Pop the smallest from the heap and append to merged list
        # Push next node from same linked list into the heap
        # Return head of the merged list

        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))  # Store (val, index, node)
                # Heap => [(1, 0, 1->4->5), (1, 1, 1->3->4), [2, 2, 2->6]]
        
        dummy = ListNode()
        current = dummy

        while heap:
            # Pop the smallest node
            val, i, node = heapq.heappop(heap)
            # Pop (1, 0, 1->4->5) from the heap => Add it to the merged list
            current.next = node
            current = current.next
            # Push next node (4->5) into the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                # Heap => [(1, 1, 1->3->4), (2, 2, 2->6), (4, 0, 4->5)]
        
        return dummy.next
