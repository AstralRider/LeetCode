class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        countMap = {}

        for task in tasks:
          countMap[task] = 1 + countMap.get(task, 0)

        maxHeap = [-task for task in countMap.values()]
        heapq.heapify(maxHeap)

        queue = collections.deque()

        time = 0

        while maxHeap or queue:
          time += 1

          if maxHeap:
            count = heapq.heappop(maxHeap)
            count += 1
            if count:
              queue.append([count, time + n])

          if queue and queue[0][1] == time:
            heapq.heappush(maxHeap, queue.popleft()[0])
        
        return time

          




          
