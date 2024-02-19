class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        L = 0 
        R = L + 1
        while R < len(prices):
          if prices[R] < prices[L]:
            L = R
            R += 1
          else:
            profit = max(prices[R] - prices[L], profit)
            
            R += 1
        return profit
