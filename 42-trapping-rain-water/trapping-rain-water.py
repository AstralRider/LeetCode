class Solution:
    def trap(self, height: List[int]) -> int:

        maxL = height[0]
        maxR = height[-1]

        l = 0
        r = len(height) - 1

        total_water = 0

        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(height[l], maxL)
                top = min(maxL, maxR)
                water = top - height[l]

                if water > 0:
                    total_water += water

            else:
                r -= 1
                maxR = max(height[r], maxR)
                top = min(maxL, maxR)
                water = top - height[r]

                if water > 0:
                    total_water += water    
                                   
        return total_water
