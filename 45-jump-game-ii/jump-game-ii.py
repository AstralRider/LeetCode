class Solution:
    def jump(self, nums: List[int]) -> int:
        
        cache = [float('inf')] * len(nums)

        def dfs(i):
            if i >= len(nums) - 1:
                return 0
            
            if cache[i] != float('inf'):
                return cache[i]
            
            

            for j in range(1, nums[i] + 1):
               cache[i] = min(dfs(i + j) + 1, cache[i])
            
            return cache[i]
        
        return dfs(0)
        