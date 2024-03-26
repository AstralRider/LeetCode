# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.kth = None
        self.dfs(root, k)
        return self.kth

  
    
    def dfs(self, root, k):
      if root is None:
        return
        
      self.dfs(root.left, k)
      
      #Remember to increment count and check count after visiting left
      self.count += 1

      if self.count == k:
        self.kth = root.val
        return

      self.dfs(root.right, k)

    #Extend basic in order traversal
    # def inorder(root):
    # if not root:
    #     return    
    # inorder(root.left)
    # print(root.val)
    # inorder(root.right)


