class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        def rob_linear(nums):
            cache = {}

            def dfs(i):
                if i in cache:
                    return cache[i]
                
                if i >= len(nums):
                    return 0
                
                rob = dfs(i + 2) + nums[i]
                skip = dfs(i + 1)
                
                cache[i] = max(rob, skip)
                return cache[i]
            
            return dfs(0)
        
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))