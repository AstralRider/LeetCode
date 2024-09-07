class Solution:
    def reorganizeString(self, s: str) -> str:
        charMap = {}
        maxHeap = []
        res = ""
        queue = collections.deque()

        #O(N)
        for char in s:
            charMap[char] = 1 + charMap.get(char, 0)
        
        #(N)
        for char, cnt in charMap.items():
            maxHeap.append((-cnt, char))
        
        #O(N)
        heapq.heapify(maxHeap)

        while maxHeap:
            cnt, char = heapq.heappop(maxHeap)
            cnt += 1
            res += char

            if queue:
                pair = queue.popleft()
                heapq.heappush(maxHeap, pair)

            if cnt < 0:
                queue.append((cnt, char))
            
        if len(res) == len(s):
            return res
        else:
            return ""
        





            
        
