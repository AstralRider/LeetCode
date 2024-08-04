class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) < 3:
            return max(nums)

        cache = {}

        def dfs(i, j):
            if i in cache:
                return cache[i]

            if i > j:
                return 0
            
            rob = dfs(i + 2, j)  + nums[i]
            skip = dfs(i + 1, j)

            cache[i] = max(rob, skip)
            return cache[i]
        
        
        res1 = dfs(0, len(nums) - 2)
        cache.clear()
        res2 = dfs(1, len(nums) - 1)
        return max(res1, res2)