class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        counter = 0
        total = 0
        l = 0
        for r in range(len(arr)):
            total += arr[r]

            if (r-l+1) < k:
                continue

            if (r-l+1) > k:
                total -= arr[l]
                l += 1
            
            if total / k >= threshold:
                counter += 1

        return counter

        #total = 6
        #window_size = (1), (2), (3), (4) (3), 
        #total / k = 2
        #[2,2,2,2,5,5,5,8]
        #counter = 0
