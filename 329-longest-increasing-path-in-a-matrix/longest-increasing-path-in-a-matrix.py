class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        # key: (r,c)
        cache = {}

        ROW = len(matrix)
        COLS = len(matrix[0])

        def dfs(r, c, prev):
            if r < 0 or r == ROW:
                return 0

            if c < 0 or c == COLS:
                return 0
            
            if prev >= matrix[r][c]:
                return 0

            if (r, c) in cache:
                return cache[r, c]
                
            cache[r, c] = 0
            cache[r, c] = max(
                dfs(r + 1, c, matrix[r][c]) + 1,
                dfs(r - 1, c, matrix[r][c]) + 1,
                dfs(r, c + 1, matrix[r][c]) + 1,
                dfs(r, c - 1, matrix[r][c]) + 1,
            )

            return cache[r, c]
        
        res = 0

        for r in range(ROW):
            for c in range(COLS):
                res = max(dfs(r, c, float("-inf")), res)
        print(cache)
        return res
