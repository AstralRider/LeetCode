class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        counter = 0
        total = 0
        l = 0
        for r in range(len(arr)):
            total += arr[r]
            
            if (r-l+1) > k:
                total -= arr[l]
                l += 1
            
            if total / k >= threshold and (r-l+1) == k:
                counter += 1

        return counter
