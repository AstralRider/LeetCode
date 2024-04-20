class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                r,c = q.popleft()
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                
                #look left, right, up and down for the current node
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    #check in range, node == 1 and not already visited
                    if (row in range(ROWS) and col in range(COLS) and grid[row][col] == "1" and (row,col) not in visited):
                        q.append((row,col))
                        visited.add((row,col))

        for r in range(ROWS):
            for c in range (COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands

        