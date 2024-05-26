class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]

        if n < 2:
            return dp[0]

        i = 2

        while i < n:
            tmp = dp[1]
            dp[1] = tmp + dp[0]
            dp[0] = tmp
            i += 1
        
        return dp[1]