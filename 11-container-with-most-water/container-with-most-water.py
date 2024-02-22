class Solution:
    def maxArea(self, height: List[int]) -> int:
      area = 0

      L = 0
      R = len(height) - 1

      while L < R:
        top = min(height[L], height[R])
        area = max(area, top * (R - L))
        if height[L] < height[R]:
          L += 1
        else:
          R -= 1
      return area

