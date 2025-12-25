# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Step 1: Find length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # If removing head itself
        if n == length:
            return head.next

        # Step 2: Reach (length-n)th node
        curr = head
        for _ in range(length - n - 1):
            curr = curr.next

        # Step 3: Delete next node
        curr.next = curr.next.next
        
        return head
