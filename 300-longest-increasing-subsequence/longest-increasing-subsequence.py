class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        cache = {}
        
        def dfs(i, cache):
            if i in cache:
                return cache[i]

            if i == len(nums):
                return 0
            
            cache[i] = 1

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    cache[i] = max(cache[i], dfs(j, cache) + 1)
            
            return cache[i]
        res = 1
        for n in range(len(nums)):
            res = max(res, dfs(n, cache))
        
        return res

        #10
#     9 2 5 3
#    2 5

#      
#