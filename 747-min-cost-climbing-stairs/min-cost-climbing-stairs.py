class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost)-3, -1, -1):
            price = cost[i]
            cost[i] = min((price + cost[i+1]), ((price + cost[i+2])))
        return min(cost[0], cost[1])
            


