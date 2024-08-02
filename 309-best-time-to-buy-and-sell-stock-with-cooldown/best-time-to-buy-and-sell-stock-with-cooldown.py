class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cache = {}

        def dfs(i, buy):
            if i >= len(prices):
                return 0
            
            if (i, buy) in cache:
                return cache[i, buy]
            
            cache[i, buy] = 0
            if buy:
                cooldown = dfs(i + 1, buy)
                bought = dfs(i + 1, False) - prices[i]
                cache[i, buy] = max(cooldown, bought)
            else:
                cooldown = dfs(i + 1, buy)
                sell = dfs(i + 2, True) + prices[i]
                cache[i, buy] = max(cooldown, sell)
            
            return cache[i, buy] 
        return dfs(0, True)





            
      