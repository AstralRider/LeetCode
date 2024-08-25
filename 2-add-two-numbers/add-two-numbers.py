# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = l1
        p2 = l2
        carry = 0
        dummy = ListNode(-1)
        curr = dummy

        while p1 or p2 or carry:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0

            curr_total = v1 + v2 + carry
            ones_place = curr_total % 10
            carry = curr_total // 10

            curr.next = ListNode(ones_place)
            curr = curr.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        return dummy.next
