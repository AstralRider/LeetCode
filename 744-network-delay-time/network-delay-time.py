import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {}
        
        output = {}

        for i in range (1, n + 1):
            adjList[i] = []
        
        for src, dst, weight in times:
            adjList[src].append([dst, weight])
        
        minHeap = [[0, k]]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in output:
                continue
            output[n1] = w1

            for n2, w2 in adjList[n1]:
                if n2 not in output:
                    heapq.heappush(minHeap, [w2 + w1, n2])

        if len(output) != n:
            return -1
        else:
            return max(output.values())



        
