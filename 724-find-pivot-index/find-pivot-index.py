class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        res = [0] * len(nums)
        pre = 0
        post = 0
        
        for j in range(len(nums)-1, -1, -1):
            post += nums[j]
            res[j] = post
        
        for i in range(len(nums)):
            pre += nums[i]
            if res[i] == pre:
                return i

            
        

        
            
        
        return -1


