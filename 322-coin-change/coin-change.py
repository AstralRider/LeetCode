class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dfs(remaining, cache):
            if remaining in cache:
                return cache[remaining]
            
            if remaining == 0:
                return 0
            
            if remaining < 0:
                return float("inf")
            
            min_coins = float("inf")

            for coin in coins:
                include = dfs(remaining - coin, cache) +1 
                min_coins = min(min_coins, include)

            cache[remaining] = min_coins

            return min_coins
        
        res = dfs(amount, {0:0})

        if res == float("inf"):
            return -1
        else:
            return res