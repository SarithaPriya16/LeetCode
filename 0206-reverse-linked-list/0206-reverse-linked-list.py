# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur=head
        prev=None
        while cur:
            nxt = cur.next       # store next
            cur.next = prev      # reverse pointer
            prev = cur           # move prev forward
            cur = nxt
        return prev
           
    