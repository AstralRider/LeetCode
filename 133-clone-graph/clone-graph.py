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
        
        cloneMap = {}
        
        def dfs(node):
            if node in cloneMap:
                return cloneMap[node]

            clone = Node(node.val)

            cloneMap[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone


        if node:
            return dfs(node)
        else:
            return node

        