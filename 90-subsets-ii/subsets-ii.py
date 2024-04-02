class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets, curSet = [], []
        nums.sort() #important for duplicates

        def helper(i, nums, curSet, subsets):
          if i >= len(nums):
            subsets.append(curSet.copy())
            return
          
          curSet.append(nums[i])
          helper(i + 1, nums, curSet, subsets)
          curSet.pop()

          while i + 1 <len(nums) and nums[i + 1] == nums[i]: #important for duplicates
            i += 1
          helper(i + 1, nums, curSet, subsets)
        
        helper(0, nums, curSet, subsets)
        return subsets
