import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)

        res = R

        while L <= R:
          k = (L + R) // 2

          hours = 0

          for p in piles:
            hours += math.ceil(p/k)
          
          if hours > h:
            L = k + 1
          elif hours <= h:
            res = min(k, res)
            R = k - 1
        return res

# 0 - 11

#           


