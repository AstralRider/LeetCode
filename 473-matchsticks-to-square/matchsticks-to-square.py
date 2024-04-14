class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
    
        total = 0
        for n in matchsticks:
            total += n
        
        if total % 4 != 0:
            return False
        
        target = total // 4

        used = [False] * len(matchsticks)

        def backtrack(i, sides, sideSum):
            if sides == 0:
                return True
            if sideSum == target:
                return backtrack(0, sides -1, 0)
            
            for j in range(i, len(matchsticks)):
                if used[j] or sideSum + matchsticks[j] > target:
                    continue
                used[j] = True

                if backtrack(j + 1, sides, sideSum + matchsticks[j]):
                    return True

                used[j] = False
            return False
        return backtrack(0, 4, 0) 

            
