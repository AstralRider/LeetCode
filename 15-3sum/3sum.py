class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #
        #[-4, -1, -1, 0, 1, 2]
        res = []
        #nlogn
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r and l < len(nums):
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1 
                    r -= 1
                    while nums[l] == nums[l-1] and nums[r] == nums[r+1] and l<r:
                        l += 1
        return res

