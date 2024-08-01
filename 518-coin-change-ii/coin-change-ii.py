class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        cache = {}

        def dfs(i, total):

            if i == len(coins):
                return 0
            
            if total > amount:
                return 0
            
            if (i, total) in cache:
                return cache[i, total]
            
            if total == amount:
                return 1
            
            cache[i, total] = 0
            for j in range(i, len(coins)):
                cache[i, total] += dfs(j, total + coins[j]) 
            
            return cache[i, total]
        return dfs(0, 0)

            