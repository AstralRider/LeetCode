# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #reverse linked list
        #two pointers and find nodes smaller

        curr = head
        prev = None

        while curr:
            fast = curr.next
            curr.next = prev
            prev = curr
            curr = fast
        
        p1 = prev
        p2 = prev.next

        while p2:
            if p2.val < p1.val:
                p2 = p2.next
            else:
                p1.next = p2
                p1 = p2
                p2 = p2.next
        p1.next = p2
        
        new_curr = prev
        new_prev = None

        while new_curr:
            new_fast = new_curr.next
            new_curr.next = new_prev
            new_prev = new_curr
            new_curr = new_fast

        return new_prev
    
