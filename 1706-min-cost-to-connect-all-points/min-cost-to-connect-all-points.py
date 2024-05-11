import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adjList = {}
        
        nodes = len(points)

        for i in range(nodes):
            adjList[i] = []

        # O(n^2)
        for i in range(nodes):
            x1, y1 = points[i]
            for j in range(i+1, nodes):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                adjList[i].append([j, distance])
                adjList[j].append([i, distance])
        
        res = 0

        visit = set()
        minHeap = []

        for node, weight in adjList[0]:
            heapq.heappush(minHeap, [weight, 0, node])
        
        visit.add(0)

        while len(visit) < nodes:
            weight, src, dst = heapq.heappop(minHeap)
            if dst in visit:
                continue
            
            visit.add(dst)

            res += weight

            for node, weight in adjList[dst]:
                if node not in visit:
                    heapq.heappush(minHeap, [weight, dst, node])
        
        return res



