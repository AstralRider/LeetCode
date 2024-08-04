class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]

            if i >= len(nums):
                return 0
            
            rob = dfs(i + 2)
            skip = dfs(i + 1)

            cache[i] = max(rob + nums[i], skip)
            return cache[i]
        
        return dfs(0)