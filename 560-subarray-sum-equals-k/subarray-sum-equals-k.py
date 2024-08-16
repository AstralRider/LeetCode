class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sum_map = {0:1}

        prefix_sum = 0

        count = 0

        for n in nums:
            prefix_sum += n

            difference = prefix_sum - k

            if difference in sum_map:
                count += sum_map[difference]
            
            sum_map[prefix_sum] = 1 + sum_map.get(prefix_sum, 0)
        
        return count


