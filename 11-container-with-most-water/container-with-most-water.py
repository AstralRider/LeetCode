class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        volume = 0 

        L = 0
        R = len(height) - 1

        while L < R:
            distance = R - L
            ceiling = min(height[L], height[R])
            volume = max(volume, (distance * ceiling))
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return volume
