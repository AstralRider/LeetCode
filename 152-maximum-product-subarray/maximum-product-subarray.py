class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_val = 1
        min_val = 1

        #O(N)
        res = max(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                max_val, min_val = 1, 1
                continue
            
            tmp = max_val * nums[i]
            max_val = max(max_val * nums[i], min_val * nums[i], nums[i])
            min_val = min(tmp, min_val * nums[i], nums[i])
            
            res = max(max_val, res)
        
        return res

        

        


        

        #[2,3,-2,4]

# 