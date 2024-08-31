# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        def dfs(root):
            if not root:
                return False

            mid = root == p or root == q            
            left = dfs(root.left)
            right = dfs(root.right)

            
            if left + right + mid >= 2:
                self.res = root
        
            return left or right or mid

        dfs(root)
        return self.res