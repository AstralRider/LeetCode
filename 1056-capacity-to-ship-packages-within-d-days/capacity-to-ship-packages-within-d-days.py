class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        #minimum weight has to be max(weights)
        #max weight has to be sum(weights) in case we need to ship everything in a single day

        l = max(weights)
        r = sum(weights)
        res = float("inf")

        def canShip(capacity):
            days_required = 1
            total = 0

            for weight in weights:
                if total + weight <= capacity:
                    total += weight
                else:
                    total = weight
                    days_required += 1
            if days_required <= days:
                return True
            else:
                return False
            

        while l <= r:
            mid = (l + r) // 2
            if canShip(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res 

#Time O(N * log(sum(weights) - max(weights)))