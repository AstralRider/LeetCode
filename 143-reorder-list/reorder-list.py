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
        slow = head
        fast = head.next
        while fast and fast.next:
          slow = slow.next
          fast = fast.next.next
        
        prev = None
        #ref to second half of list
        curr = slow.next
        
        #break link between first and second half of list
        slow.next = None
        
        while curr:
          tmp = curr.next 
          curr.next = prev
          prev = curr
          curr = tmp
        
        second = prev
        first = head

        while second:
          tmp1 = first.next
          tmp2 = second.next

          first.next = second
          second.next = tmp1

          first = tmp1
          second = tmp2