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
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l2 = slow.next
        slow.next = None

        prev = None
        curr = l2
        
        while curr:
            fast = curr.next
            curr.next = prev
            prev = curr
            curr = fast


        l1 = head
        while l1 and prev:
            tmp1 = l1.next
            tmp2 = prev.next
            l1.next = prev
            prev.next = tmp1
            l1 = tmp1
            prev = tmp2







