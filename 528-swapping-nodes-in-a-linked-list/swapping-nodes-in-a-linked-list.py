# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        tmp = k
        
        end = head
        slow = dummy

        while k:
          k -= 1
          end = end.next
        
        while end:
          end = end.next
          slow = slow.next
        
        swap1 = slow.next

        start = head
        counter = 1
        while start:
          if counter == tmp:
            break
          start = start.next
          counter += 1
        
        start.val, swap1.val = swap1.val, start.val

        return dummy.next