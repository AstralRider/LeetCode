class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        #dfs or bfs
        # use a set to track visited 1's
        # if it is a 1 we haven't seen before, increment islands by 1
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        numberOfIslands = 0

        def dfs(r,c,visited):
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or grid[r][c] == "0"
                or (r,c) in visited):
                    return
            
            visited.add((r,c))

            dfs(r+1,c, visited)
            dfs(r-1,c, visited)
            dfs(r,c+1, visited)
            dfs(r,c-1, visited)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == "1":
                    dfs(r,c,visited)
                    numberOfIslands += 1

        return numberOfIslands



