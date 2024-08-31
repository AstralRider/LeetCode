# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root_1, root_2):
            if not root_1 and not root_2:
                return None
            
            val1 = root_1.val if root_1 else 0
            val2 = root_2.val if root_2 else 0
            root = TreeNode(val1 + val2)

            root.left = dfs(root_1.left if root_1 else None, root_2.left if root_2 else None)
            root.right = dfs(root_1.right if root_1 else None, root_2.right if root_2 else None)

            return root
        return dfs(root1, root2)

