class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        k = 1
      
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[k] = nums[r]
                k += 1
            
        return k
