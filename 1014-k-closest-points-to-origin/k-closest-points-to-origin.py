class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []

        for point in points:
          x = point[0]
          y = point[1]

          distance = math.sqrt((x - 0)**2 + (y - 0) ** 2)
          minHeap.append((distance, x, y))    
        heapq.heapify(minHeap)

        while k > 0:
          dist,x,y = heapq.heappop(minHeap)
          k -= 1
          res.append([x, y])
        
        return res


