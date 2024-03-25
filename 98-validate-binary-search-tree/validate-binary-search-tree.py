# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

      return self.dfs(root, float("-inf"), float("inf"))
    
    def dfs(self, root, lower_bound, upper_bound):
        if not root:
            return True
        
        if root.val <= lower_bound or root.val >= upper_bound:
          return False
        
        return (self.dfs(root.left, lower_bound, root.val) and
                self.dfs(root.right, root.val, upper_bound))
    
      
