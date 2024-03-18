# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
          return []
        
        length = 0
        curr = head
        while curr:
          curr = curr.next
          length += 1
        node_to_remove = length - n

        if length < 2:
          return

        curr = head
        prev = None
        pos = 0
        while pos < node_to_remove:
          prev = curr
          curr = curr.next
          pos += 1

        if curr:
          if not curr.next:
            prev.next = None
          elif not prev:
            curr=curr.next
            head = curr
          else:
            prev.next = curr.next
        
        return head
  
          

        
        