class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        result = []
        def backtrack(i, res):
            if len(res) == len(nums):
                if res in nums:
                    return False
                else:
                    result.append(res)
                    return True
            
            for j in range(i, len(nums)):
                if backtrack(j + 1, res + "1"):
                    return True
                if backtrack(j + 1, res + "0"):
                    return True

        backtrack(0, "")
        return result[0]


            
