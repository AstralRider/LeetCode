class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        l = 1
        r = n

        res = 1

        while l <= r:
            mid = (l + r) // 2

            total = (mid/2)*(mid + 1)

            if n >= total:
                l = mid + 1
                res = mid
            else:
                r = mid - 1
        
        return res


            
# 1, 2, 3, 4, 5
#
