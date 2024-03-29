class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        countMap = {}
        
        #O(N)
        for task in tasks:
          countMap[task] = 1 + countMap.get(task, 0)

        #O(26)
        maxHeap = [-task for task in countMap.values()]

        #O(26)
        heapq.heapify(maxHeap)

        queue = collections.deque()

        time = 0


        while maxHeap or queue:
          time += 1

          if maxHeap:
            #O(Log * 26)
            count = heapq.heappop(maxHeap)
            count += 1
            if count:
              queue.append([count, time + n])

          if queue and queue[0][1] == time:
            #O(Log * 26)
            heapq.heappush(maxHeap, queue.popleft()[0])
        
        return time

          




          
