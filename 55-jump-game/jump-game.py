class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        print(goal)
        if goal == 0:
            return True
        else:
            return False
