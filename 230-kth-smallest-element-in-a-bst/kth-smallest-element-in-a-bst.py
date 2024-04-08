# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.heap = []
        self.dfs(root)
        self.kth = 0

        heapq.heapify(self.heap)

        while k:
            self.kth = heapq.heappop(self.heap)
            k -= 1
        
        return self.kth

    
    def dfs(self, root):
        if not root:
            return None
        
        self.heap.append(root.val)

        self.dfs(root.left)
        self.dfs(root.right)
        
    