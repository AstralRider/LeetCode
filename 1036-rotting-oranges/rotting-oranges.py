from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        orangesCount = 0
        minutes = 0
        queue = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))
                if grid[i][j] == 1:
                    orangesCount += 1
        
        if orangesCount == 0:
            return 0
        

        while queue:
            if orangesCount > 0:
                minutes += 1
                        
            for i in range(len(queue)):
                r, c = queue.popleft()

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if (
                        min(new_r, new_c) < 0
                        or new_r == ROWS
                        or new_c == COLS
                        or (new_r, new_c) in visited
                        or grid[new_r][new_c] == 0
                    ):
                        continue
                    else:
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c))
                        orangesCount -= 1
            
            
        
        if orangesCount > 0:
            return -1 
        else:
            return minutes
        

