# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
          return True
        
        if not root:
          return False
        
        if self.dfs(root, subRoot):
          return True
        else:
          return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
        
    def dfs(self, root, subRoot):
      if not root and not subRoot:
        return True
        
      while root and subRoot and root.val == subRoot.val:
        return self.dfs(root.right, subRoot.right) and self.dfs(root.left, subRoot.left)
      return False