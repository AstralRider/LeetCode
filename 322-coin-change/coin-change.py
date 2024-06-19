class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(remainder, coins, cache):
            if remainder in cache:
                return cache[remainder]

            if remainder == 0:
                return 0
            
            if remainder < 0:
                return float("inf")
            
            cache[remainder] = float("inf")
            for coin in coins:
                    cache[remainder] = min(cache[remainder], dfs(remainder - coin, coins, cache) + 1)
            
            return cache[remainder]
        
        res = dfs(amount, coins, cache)

        if res == float("inf"):
            return -1
        else:
            return res

