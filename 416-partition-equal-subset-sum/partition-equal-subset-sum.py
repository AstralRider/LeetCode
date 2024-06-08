class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        memo = {}
        def dfs(i, currSum, target, nums, memo):
            if (i, currSum) in memo:
                return memo[(i, currSum)]
            
            if i == len(nums) or currSum > target:
                memo[(i, currSum)] = False
                return False
            
            if currSum == target:
                memo[(i, currSum)] = True
                return True
            
            skip = dfs(i + 1, currSum, target, nums,memo)
            include = False
            if nums[i] + currSum <= target:
                include = dfs(i + 1, nums[i] + currSum, target, nums, memo)
            
            res = skip or include
            memo[(i, currSum)] = res
            return memo[(i, currSum)]
   
        
        return dfs(0, 0, target, nums,memo)


            
                
