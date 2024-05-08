class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        
        res = 0

        r = len(nums) - 1
        l = 0

        while l <= r:
            if nums[l] + nums[r] <= target:
                res += 2**(r-l)
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
        return res % (10**9 + 7)

        

            
            