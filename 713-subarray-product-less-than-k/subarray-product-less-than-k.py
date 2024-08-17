class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        product = 1

        res = 0

        L = 0

        for R in range(len(nums)):
            product *= nums[R]

            while product >= k and L <= R:
                product //= nums[L]
                L += 1
            res += (R - L + 1)
        
        return res



        