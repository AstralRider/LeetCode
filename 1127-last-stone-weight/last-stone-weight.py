class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap = [-stone for stone in stones]
        heapq.heapify(self.maxHeap)

        while len(self.maxHeap) > 1:
          y = heapq.heappop(self.maxHeap)
          x = heapq.heappop(self.maxHeap)

          if x != y:
            y = y - x
            heapq.heappush(self.maxHeap, y)
        self.maxHeap.append(0)
        return abs(self.maxHeap[0] )
