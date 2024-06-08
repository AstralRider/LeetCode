class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = 0
        for n in nums:
            total += n
            
        print(total/2)
        if total % 2 != 0:
            return False

        target = total / 2
        memo = {}
        def dfs(i, currSum, target, nums, memo):
            if i == len(nums):
                return False
            if (i, currSum) in memo:
                return memo[(i, currSum)]
            if currSum == target:
                return True
            
            skip = dfs(i + 1, currSum, target, nums,memo)
            include = False
            if nums[i] + currSum <= target:
                include = dfs(i + 1, nums[i] + currSum, target, nums, memo)
            
            res = skip or include
            memo[(i, currSum)] = res
            return memo[(i, currSum)]
   
        
        return dfs(0, 0, target, nums,memo)


            
                
