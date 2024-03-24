from collections import deque 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.output = []
        
        queue = deque()

        if root:
          queue.append(root)
        
        while len(queue) > 0:
          
          rightMost = None
          for i in range(len(queue)):
            curr = queue.popleft()
            rightMost = curr
            if curr.left:
              queue.append(curr.left)
            if curr.right:
              queue.append(curr.right)

          #right most will always be last node in a level
          #we append the node last set as rightMost after scanning the level is done
          self.output.append(rightMost.val)
        
        return self.output




     
      
