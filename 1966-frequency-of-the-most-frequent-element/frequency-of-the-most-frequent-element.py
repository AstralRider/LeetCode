class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        l = 0
        total = 0
        elements = 0

        for r in range(len(nums)):
            total += nums[r]
            while (nums[r] * (r-l + 1)) > total + k:
                total -= nums[l]
                l += 1
            elements = max(elements, (r-l)+1)

        return elements
        
                

            


            

            
