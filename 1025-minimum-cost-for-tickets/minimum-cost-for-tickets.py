class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        cache = {}
        
        def dfs(i, cache):
            if i in cache:
                return cache[i]

            if i == len(days):
                return 0
            
            j = i
            travel = [1, 7, 30]
            cache[i] = float("inf")
            for t in range(len(travel)):
                while j < len(days) and days[j] < days[i] + travel[t]:
                    j += 1
                res = dfs(j, cache) + costs[t]
                cache[i] = min(cache[i], res)

            return cache[i]
        
        return dfs(0, cache)

                
                
             
            
            