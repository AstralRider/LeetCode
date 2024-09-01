class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heap.append(stone * -1)

        heapq.heapify(heap)

        while len(heap) >= 2:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            if x == y:
                continue
            else:
                new_stone = abs(y - x)
                heapq.heappush(heap, -1 * new_stone)

        if len(heap) > 0:
            return heap[0] * -1
        else:
            return 0 