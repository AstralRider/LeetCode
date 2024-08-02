class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}
        def dfs(i, amount):
            if (i, amount) in cache:
                return cache[i,amount]

            if i == len(nums) and amount == target:
                return 1
            
            if i == len(nums):
                return 0 
            
            cache[i,amount] = 0
            cache[i,amount] += dfs(i + 1, amount + nums[i]) + dfs(i + 1, amount - nums[i])

            return cache[i,amount]
        return dfs(0, 0)