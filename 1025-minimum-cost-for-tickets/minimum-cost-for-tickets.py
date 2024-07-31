class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        cache = {}
        
        def dfs(i, cache):
            if i in cache:
                return cache[i]

            if i == len(days):
                return 0
            

            cache[i] = float("inf")

            l = i
            passes = [1, 7, 30]

            for k in range(len(costs)):

                while l < len(days) and days[l] < passes[k] + days[i]:
                    l += 1
                
                cache[i] = min(dfs(l, cache) + costs[k], cache[i])
            
            return cache[i]
        
        return dfs(0, cache)






#              * + 7
            # [1,4,6,7,8,20] 


