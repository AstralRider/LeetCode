import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        N = len(grid)

        visit = set()

        minHeap = [[grid[0][0], 0, 0]]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit.add((0,0))

        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            if r == N - 1 and c == N - 1:
                return t

            for dr, dc in directions:
                neiR = dr + r
                neiC = dc + c
                if (neiR == N or neiC == N or min(neiR, neiC) < 0 or (neiR, neiC) in visit):
                    continue
                visit.add((neiR, neiC))

                heapq.heappush(minHeap, [max(t, grid[neiR][neiC]), neiR, neiC])



