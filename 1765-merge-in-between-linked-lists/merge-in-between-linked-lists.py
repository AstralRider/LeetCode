# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        next_node = list1

        dummy = ListNode(-1)
        dummy.next = list1
        
        a_node = dummy
        b_node = list1
        list2_last_node = list2
        
        while b:
            b_node = b_node.next
            b -= 1
        
        while a:
            a_node = a_node.next
            a -= 1
        
        while list2_last_node.next:
            list2_last_node = list2_last_node.next
        
        a_node.next = list2
        list2_last_node.next = b_node.next

        return dummy.next

