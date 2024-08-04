class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]

            if i >= len(cost):
                return 0
            
            one = dfs(i + 1)
            two = dfs(i + 2)

            cache[i] = min(one, two) + cost[i]
            
            return cache[i]
        
        return min(dfs(0), dfs(1))