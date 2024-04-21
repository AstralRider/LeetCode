"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        nodeMap = {}

        def deepCopy(node):
            if node in nodeMap:
                return nodeMap[node]
            
            clone = Node(node.val)
            nodeMap[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(deepCopy(neighbor))
            return clone
        return deepCopy(node)

        

