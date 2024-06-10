class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        minCount = -1
        cache = {}
        def dfs(i, currSum, cache):
            if (i, currSum) in cache:
                return cache[(i, currSum)]

            if currSum == amount:
                return 0
            
            if i >= len(coins) or currSum > amount:
                return float("inf")

            skip = dfs(i + 1, currSum, cache)
            
            include = float("inf")
            if currSum + coins[i] <= amount:
                include = dfs(i, currSum + coins[i], cache)

                if include != float("inf"):
                    include += 1

            if skip > -1 and include > -1:
                cache[(i, currSum)] = min(skip, include)
                return cache[(i, currSum)]
            elif skip > -1:
                return skip
            elif include > -1:
                return include
            else:
                return -1
        
        
        res = dfs(0,0, cache)
        return res if res != float("inf") else -1

            
