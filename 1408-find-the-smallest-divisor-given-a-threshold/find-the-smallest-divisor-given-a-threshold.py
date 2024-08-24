class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        #min = 1
        #max = max(nums)
        l = 1
        r = max(nums)
        res = float("inf")
        while l <= r:
            mid = (l + r) // 2
            total = 0
            for n in nums:
                total += math.ceil(n / mid)
            
            if total <= threshold:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res

#O(N * log(max(nums)))



