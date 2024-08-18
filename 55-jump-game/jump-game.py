class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] + i-1 >= goal:
                goal = i - 1
        print(goal)
        if goal == 0:
            return True
        else:
            return False
