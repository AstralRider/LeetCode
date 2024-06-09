class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, currSum, nums, cache):
            if i == len(nums) and currSum == target:
                return 1
            if i >= len(nums):
                return 0
            
            if (i, currSum) in cache:
                return cache[(i, currSum)]
            
            res = dfs(i + 1, currSum - nums[i], nums, cache) + dfs(i + 1, currSum + nums[i], nums, cache)
            cache[(i, currSum)] = res
            
            return res
        
        cache = {}
        return dfs(0, 0, nums, cache)