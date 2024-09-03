class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        #O(N)
        for num in nums:
            #O(logk) not logn since our heap will never have more than k elements because we pop them
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
