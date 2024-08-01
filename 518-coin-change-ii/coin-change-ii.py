class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        cache = {}

        def dfs(i, total):

            if total == amount:
                return 1

            if i == len(coins):
                return 0
            
            
            
            if (i, total) in cache:
                return cache[i, total]

            cache[i, total] = 0
            for j in range(i, len(coins)):
                if total + coins[j] <= amount:
                    cache[i, total] += dfs(j, total + coins[j]) 
                
            
            return cache[i, total]
        return dfs(0, 0)

            