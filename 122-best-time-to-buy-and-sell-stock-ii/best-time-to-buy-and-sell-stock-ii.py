class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      maxP = 0

      for i in range(1, len(prices)):
        maxP += max(0, prices[i] - prices[i - 1])
      
      return maxP
