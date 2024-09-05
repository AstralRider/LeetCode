class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        countMap = {}

        minHeap = []

        #O(N)
        for n in arr:
            countMap[n] = 1 + countMap.get(n, 0)
        
        #O(N)
        for count in countMap.values():
            minHeap.append(count)
        
        #O(N)
        heapq.heapify(minHeap)

        #(k * logN)
        while k > 0:
            cnt = heapq.heappop(minHeap)
            tmp = cnt
            cnt -= k
            k -= tmp
            if cnt > 0:
                heapq.heappush(minHeap, cnt)
        
        return len(minHeap)
