class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #dfs or bfs
        #find all the 1's connected the current node
        #add these positions to a set
        #if we encounter it again when running dfs/bfs, we skip it

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        islands = 0

        def dfs(r,c):
            if (
                min(r,c) < 0
                or r == ROWS
                or c == COLS
                or (r,c) in visited
                or grid[r][c] == "0"
            ):
                return
            
            visited.add((r,c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r,c +  1)
            dfs(r,c -  1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        return islands

        