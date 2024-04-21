class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        self.island = 0

        def bfs(r,c):
            visited.add((r,c))
            q = collections.deque()
            q.append((r,c))

            size = 0

            while q:
                r,c = q.popleft()
                size += 1
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    new_row = r + dr
                    new_col = c + dc
                    if new_row in range(ROWS) and new_col in range(COLS) and (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))
            return size




        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    self.island = max(bfs(r,c), self.island)

        return self.island
