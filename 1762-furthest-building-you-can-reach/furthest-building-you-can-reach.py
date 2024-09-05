class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxHeap = []
        i = 0

        while i < len(heights) - 1:
            gap = heights[i+1] - heights[i]
            if gap > 0:
                heapq.heappush(maxHeap, -gap)

            if bricks - gap < 0 and ladders:
                maxGap = heapq.heappop(maxHeap)
                ladders -= 1
                bricks += (-1 * maxGap)
                

            if gap > 0 and bricks - gap >= 0:
                bricks -= gap
                i += 1
            elif gap <= 0:
                i += 1
            else:
                return i
        return i 