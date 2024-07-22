class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cache = {}

        def dfs(r,c):
            if (r,c) in cache:
                return cache[r,c]
            if r >= m:
                return 0
            if c >= n:
                return 0
            
            if r == m - 1 and c == n - 1:
                return 1

            right = dfs(r, c + 1)

            down = dfs(r + 1, c)

            cache[r,c] = right + down

            return cache[r,c]

        
        return dfs(0,0)