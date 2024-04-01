class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #for subsets, we know total number of subsets = 2^n
        subsets = []
        currSet = []
        self.helper(0, nums, subsets, currSet)
        return subsets

    def helper(self, i, nums, subsets, currSet):
      if i == len(nums):
        #O(n) operation
        subsets.append(currSet.copy())
        return
      
      currSet.append(nums[i])


      self.helper(i + 1, nums, subsets, currSet)
      #backtrack
      currSet.pop()

      self.helper(i + 1, nums, subsets, currSet)

#Time Complexity: O(n * 2^n)
#Space Complexity: O(n) for height of recursive stack