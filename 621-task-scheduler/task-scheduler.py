class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        charMap = {}
        maxHeap = []
        #O(N)
        for task in tasks:
            charMap[task] = 1 + charMap.get(task, 0)
        
        #O(N)
        for char in charMap.values():
            maxHeap.append(-1 * char)
        
        heapq.heapify(maxHeap)

        queue = collections.deque()
        time = 0
        while maxHeap or queue:
            time += 1
            if queue and queue[0][1] <= time:
                count, t = queue.popleft()
                heapq.heappush(maxHeap, count)
            
            
            if maxHeap:
                task = heapq.heappop(maxHeap)
                task += 1
                if task < 0:
                    queue.append((task, time + n + 1))

            

        return time


            


