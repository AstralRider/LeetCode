class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]

        if n <= 3:
            return n

        i = 2

        for idx in range(1, n-1):
            tmp = dp[1]
            dp[1] = tmp + dp[0]
            dp[0] = tmp
        
        return dp[1]

        #[1, 2]
        #[2, 3]
        #[3, 5]