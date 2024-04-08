# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.dfs(root, root.val)
        return self.count

    def dfs(self, root, maxVal):
        if not root:
            return None
        
        if root.val >= maxVal:
            self.count += 1
        
        maxVal = max(root.val, maxVal)
        self.dfs(root.left, maxVal)
        self.dfs(root.right, maxVal)
        

        

        
