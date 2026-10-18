# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cycle = set()

        def doRep(head: Optional[ListNode]):
            if head == None:
                return False

            if head in cycle:
                return True
            
            cycle.add(head)
            return doRep(head.next)
        
        return doRep(head)
