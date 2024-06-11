class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = [float("inf") for _ in range(amount + 1)]
        cache[0] = 0
        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    cache[a] = min(cache[a], 1 + cache[a - coin])
        
        if cache[amount] == float("inf"):
            return -1
        else:
            return cache[amount]