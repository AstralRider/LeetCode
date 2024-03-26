# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        return self.dfs(root)
    
    def dfs(self, root):
      if not root:
            return None

      left = self.dfs(root.left)
      if left is not None:
        return left

      self.count -= 1
      if self.count == 0:
        return root.val

      return self.dfs(root.right)


