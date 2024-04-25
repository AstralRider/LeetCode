"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyMap = {None: None}

        #first create every old:new pairing in the hashmap

        curr = head

        while curr:
            clone = Node(curr.val)
            copyMap[curr] = clone
            curr = curr.next
        
        curr = head
 
        while curr:
            copyMap[curr].next = copyMap.get(curr.next)
            copyMap[curr].random = copyMap.get(curr.random)
            curr = curr.next
        
        return copyMap[head]
        
