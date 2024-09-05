class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        countMap = {}

        minHeap = []

        #O(N)
        for n in arr:
            countMap[n] = 1 + countMap.get(n, 0)
        
        #O(N * logN)
        for value, count in countMap.items():
            heapq.heappush(minHeap, (count, value))

        while k > 0:
            cnt, val = heapq.heappop(minHeap)
            tmp = cnt
            cnt -= k
            k -= tmp
            if cnt > 0:
                heapq.heappush(minHeap, (cnt, val))
        
        return len(minHeap)



        #arr = [3,1,1,3,3]