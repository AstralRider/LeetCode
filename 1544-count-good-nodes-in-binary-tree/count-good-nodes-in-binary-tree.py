# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        if root:
          self.dfs(root, root.val)
        return self.count
    
    def dfs(self, root, val):
      if not root:
        return None
      
      if root.val >= val:
        self.count += 1
      
      self.dfs(root.left, max(root.val, val))
      self.dfs(root.right,  max(root.val, val))
