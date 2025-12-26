# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        while head and head.next:
            node1 = head
            node2 = head.next

            # Swapping
            prev.next = node2
            node1.next = node2.next
            node2.next = node1

            # Move pointers for next swap
            prev = node1
            head = node1.next
        
        return dummy.next