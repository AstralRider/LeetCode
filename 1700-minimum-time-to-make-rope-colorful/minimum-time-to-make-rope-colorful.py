class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        l = 0
        r = 1
        min_time = 0
        while r < len(neededTime):
            same_count = neededTime[l]
            max_seen = neededTime[l]

            if colors[r] != colors[l]:
                l += 1
                same_count = 0
                max_seen = 0

            while r < len(colors) and colors[l] == colors[r]:
                same_count += neededTime[r]
                max_seen = max(neededTime[r], max_seen)
                r += 1
            
            min_time += (same_count - max_seen)
            l = r
            r += 1
        
        return min_time