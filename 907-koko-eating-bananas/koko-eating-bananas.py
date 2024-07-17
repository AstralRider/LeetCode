class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = 0
        min_num = float("inf")

        for n in piles:
            maxPile = max(n, maxPile)
 
        l = 1 
        r = maxPile

        while l <= r:
            mid = (l + r) // 2
            total_hours = 0 
            for p in piles:
                total_hours += math.ceil(p/mid)

            if total_hours > h:
                l = mid + 1

            else: 
                r = mid - 1
                min_num = min(min_num, mid)

        return min_num



#0 1 2 3 4 5 6 7 8 9