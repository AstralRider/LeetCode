class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        res = float("inf")

        l = 1
        
        #O(N) operation
        r = max(piles)

        while l <= r:
            mid = (l + r) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)
            
            if hours <= h:
                res = min(res, mid)
                r = mid - 1
            elif hours > h:
                l = mid + 1        
        return res


