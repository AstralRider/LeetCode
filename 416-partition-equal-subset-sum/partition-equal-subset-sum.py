class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
       
        cache = [[False for _ in range(target + 1)] for _ in range(len(nums))]

        for i in range(len(nums)):
            cache[i][0] = True
        
        for i in range(1, len(nums)):
            for s in range(1, target + 1):
                if s < nums[i]:
                    cache[i][s] = cache[i-1][s]
                else:
                    cache[i][s] = cache[i-1][s] or cache[i-1][s - nums[i]]

        return cache[len(nums)-1][target]
    



            
                
