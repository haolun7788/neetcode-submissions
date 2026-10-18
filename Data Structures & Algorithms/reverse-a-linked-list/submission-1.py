# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        elif head.next == None:
            return head
        newhead = ListNode()

        prev = None
        cur = head
        nex = cur.next

        while nex != None:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        
        return prev
            
