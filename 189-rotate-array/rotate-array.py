class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        positions = nums.copy()
        
        for l in range(len(nums)):
            r = l + k
            if r < len(nums):
                nums[r] = positions[l]
            else:
                r = r % len(nums)
                nums[r] = positions[l]



        