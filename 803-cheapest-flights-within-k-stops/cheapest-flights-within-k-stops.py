class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # create an array with all the vertices set to inf
        prices = [float("inf")] * n
        
        #the cost of reaching the src node is 0
        prices[src] = 0

        for _ in range(k + 1):

            tmp = prices[:]

            for src, dest, cost in flights:
                if prices[src] == float("inf"):
                    continue
                if prices[src] + cost < tmp[dest]:
                    tmp[dest] = prices[src] + cost
            
            prices = tmp
        
        if prices[dst] == float("inf"):
            return -1
        else:
            return prices[dst]


