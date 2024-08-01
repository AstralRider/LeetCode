class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        
        def dfs(i, remaining):
            if remaining == 0:
                return 0
            if i == len(coins) or remaining < 0:
                return float('inf')
            if (i, remaining) in cache:
                return cache[(i, remaining)]
            
            # Two decisions: use current coin or move to next coin
            use_current = 1 + dfs(i, remaining - coins[i])
            skip_current = dfs(i + 1, remaining)
            
            cache[(i, remaining)] = min(use_current, skip_current)
            return cache[(i, remaining)]
        
        result = dfs(0, amount)
        return result if result != float('inf') else -1
        

