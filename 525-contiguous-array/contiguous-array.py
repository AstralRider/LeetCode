class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
       # -1 -2 -1 -2 -3 -4 -3 -2
       #[0, 0, 1, 0, 0, 0, 1, 1]

        prefix_map = {0: -1}

        prefix_sum = 0

        total = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                prefix_sum += 1
            elif nums[i] == 0:
                prefix_sum -= 1
            
            if prefix_sum in prefix_map:
                L = prefix_map[prefix_sum]
                total = max(total, (i - L))
            else:
                prefix_map[prefix_sum] = i
        
        return total
