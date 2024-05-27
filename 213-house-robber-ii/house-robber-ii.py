class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(start, end):
            h1, h2 = 0, 0 

            for i in range(start, end):
                tmp = max(h1 + nums[i], h2)
                h1 = h2
                h2 = tmp
            return h2

        return max(helper(0, len(nums)-1), helper(1, len(nums)))
