class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        nums.sort()

        def dfs(i, currSet):
            if i >= len(nums):
                res.append(currSet.copy())
                return
            currSet.append(nums[i])
            dfs(i + 1, currSet)

            currSet.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, currSet)

        
        dfs(0, [])
        return res
