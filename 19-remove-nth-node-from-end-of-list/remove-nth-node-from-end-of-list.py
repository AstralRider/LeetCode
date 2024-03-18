# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
          return []

        #use a dummy node to get the prev node of the one we need to delete
        dummy = ListNode(0, head)
        left = dummy
        right = head

        #move right n times before moving left points
        while n > 0 and right:
          n -= 1
          right = right.next

        #move L and R together
        while right:
          left = left.next
          right = right.next
        
        left.next = left.next.next
        
        #remember to return dummy.next for edge cases
        return dummy.next





  
          

        
        