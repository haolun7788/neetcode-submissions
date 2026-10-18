# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        left, right = list1, list2
        if left == None:
            return right
        elif right == None:
            return left
        
        if left.val < right.val:
            cur, head = left, left
            left = left.next
        else:
            cur, head = right, right
            right = right.next

        while left != None or right != None:
            if left == None:
                temp = right
                cur.next = temp
                cur = cur.next
                right = right.next
                continue
            elif right == None:
                temp = left
                cur.next = temp
                cur = cur.next
                left = left.next
                continue
            
            if left.val < right.val:
                cur.next = left
                cur = cur.next
                left = left.next
            else:
                cur.next = right
                cur = cur.next
                right = right.next
        
        return head
