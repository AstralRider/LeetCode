# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return root
        
        def dfs(root, total):
            if not root:
                return root
            
            if not root.left and not root.right:
                if total + root.val == targetSum:
                    return True
            
            left = dfs(root.left, total + root.val)
            right = dfs(root.right, total + root.val)

            return left or right
        return dfs(root, 0)