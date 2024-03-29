class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        #need to initialise with 0:0 for case when only 1 brick in a row
        gapMap = {0:0}

        for brick in wall:
          position = 0
          for i in range(len(brick)-1):
            position += brick[i]
            gapMap[position] = 1 + gapMap.get(position, 0)

        gaps = max(gapMap.values())
        return len(wall) - gaps