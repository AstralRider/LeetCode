# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(node):
            if not node:
                return float('inf')
            
            if not node.left and not node.right:
                return 1
            
            return 1 + min(dfs(node.left), dfs(node.right))
        
        return dfs(root)